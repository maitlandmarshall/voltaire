import { spawnSync } from "node:child_process";
import {
  copyFileSync,
  existsSync,
  mkdirSync,
  mkdtempSync,
  readdirSync,
  rmSync,
  statSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { delimiter, dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const sourcebookDirectory = resolve(scriptDirectory, "../..");
const htmlPath = join(sourcebookDirectory, "index.html");
const pdfPath = join(
  sourcebookDirectory,
  "assets",
  "output",
  "pdf",
  "voltaire-divine-rank-1.pdf",
);

function findOnPath(executableNames) {
  const pathDirectories = (process.env.PATH ?? "").split(delimiter);

  for (const directory of pathDirectories) {
    for (const executableName of executableNames) {
      const candidate = join(directory, executableName);
      if (existsSync(candidate)) {
        return candidate;
      }
    }
  }

  return undefined;
}

function findBrowser() {
  const configuredBrowser = process.env.VOLTAIRE_CHROME_PATH;
  const candidates = [
    configuredBrowser,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
  ].filter(Boolean);

  return candidates.find((candidate) => existsSync(candidate));
}

function findGhostscript() {
  const configuredGhostscript = process.env.VOLTAIRE_GHOSTSCRIPT_PATH;
  if (configuredGhostscript && existsSync(configuredGhostscript)) {
    return configuredGhostscript;
  }

  const installedCandidates = [];
  const ghostscriptRoot = "C:\\Program Files\\gs";

  if (existsSync(ghostscriptRoot)) {
    for (const versionDirectory of readdirSync(ghostscriptRoot).sort().reverse()) {
      installedCandidates.push(
        join(ghostscriptRoot, versionDirectory, "bin", "gswin64c.exe"),
        join(ghostscriptRoot, versionDirectory, "bin", "gswin32c.exe"),
      );
    }
  }

  return (
    installedCandidates.find((candidate) => existsSync(candidate)) ??
    findOnPath(
      process.platform === "win32"
        ? ["gswin64c.exe", "gswin32c.exe"]
        : ["gs"],
    )
  );
}

if (!existsSync(htmlPath)) {
  throw new Error(`Source HTML was not found: ${htmlPath}`);
}

const browserPath = findBrowser();
if (!browserPath) {
  throw new Error(
    "Chrome or Edge was not found. Set VOLTAIRE_CHROME_PATH to the browser executable.",
  );
}

mkdirSync(dirname(pdfPath), { recursive: true });

// A dedicated profile prevents a running desktop browser from intercepting the
// headless print request. The profile is temporary and contains no user state.
const profileDirectory = mkdtempSync(join(tmpdir(), "voltaire-sourcebook-"));
const expectedTempRoot = resolve(tmpdir());
const rawPdfPath = join(profileDirectory, "voltaire-divine-rank-1.raw.pdf");
const compressedPdfPath = join(
  profileDirectory,
  "voltaire-divine-rank-1.compressed.pdf",
);

try {
  const result = spawnSync(
    browserPath,
    [
      "--headless=new",
      "--disable-gpu",
      "--no-first-run",
      "--no-default-browser-check",
      "--allow-file-access-from-files",
      "--run-all-compositor-stages-before-draw",
      "--virtual-time-budget=2500",
      "--no-pdf-header-footer",
      "--generate-pdf-document-outline",
      `--user-data-dir=${profileDirectory}`,
      `--print-to-pdf=${rawPdfPath}`,
      pathToFileURL(htmlPath).href,
    ],
    {
      cwd: sourcebookDirectory,
      encoding: "utf8",
      windowsHide: true,
    },
  );

  if (result.status !== 0) {
    const diagnostic = [result.stdout, result.stderr].filter(Boolean).join("\n");
    throw new Error(`Browser PDF generation failed.\n${diagnostic}`);
  }

  if (!existsSync(rawPdfPath) || statSync(rawPdfPath).size < 100_000) {
    throw new Error("The browser returned without producing a plausible PDF.");
  }

  const ghostscriptPath = findGhostscript();

  if (ghostscriptPath) {
    const compressionResult = spawnSync(
      ghostscriptPath,
      [
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.7",
        "-dNOPAUSE",
        "-dBATCH",
        "-dQUIET",
        "-dDetectDuplicateImages=true",
        "-dDownsampleColorImages=true",
        "-dColorImageDownsampleType=/Bicubic",
        "-dColorImageResolution=240",
        "-dDownsampleGrayImages=true",
        "-dGrayImageDownsampleType=/Bicubic",
        "-dGrayImageResolution=240",
        "-dDownsampleMonoImages=true",
        "-dMonoImageResolution=600",
        `-sOutputFile=${compressedPdfPath}`,
        rawPdfPath,
      ],
      {
        cwd: sourcebookDirectory,
        encoding: "utf8",
        windowsHide: true,
      },
    );

    if (
      compressionResult.status !== 0 ||
      !existsSync(compressedPdfPath) ||
      statSync(compressedPdfPath).size < 100_000
    ) {
      const diagnostic = [
        compressionResult.stdout,
        compressionResult.stderr,
      ]
        .filter(Boolean)
        .join("\n");
      throw new Error(`Ghostscript PDF compression failed.\n${diagnostic}`);
    }

    copyFileSync(compressedPdfPath, pdfPath);
    console.log("Applied the print-quality 240 dpi Ghostscript profile.");
  } else {
    copyFileSync(rawPdfPath, pdfPath);
    console.warn(
      "Ghostscript was not found; wrote the larger browser PDF. " +
        "Set VOLTAIRE_GHOSTSCRIPT_PATH to generate the compact print edition.",
    );
  }
} finally {
  const resolvedProfile = resolve(profileDirectory);
  if (resolvedProfile.startsWith(expectedTempRoot)) {
    rmSync(resolvedProfile, { recursive: true, force: true });
  }
}

console.log(pdfPath);
