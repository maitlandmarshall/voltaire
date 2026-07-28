import { existsSync, readFileSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const sourcebookDirectory = resolve(scriptDirectory, "../..");
const htmlPath = join(sourcebookDirectory, "index.html");
const cssPath = join(sourcebookDirectory, "styles.css");
const pdfPath = join(
  sourcebookDirectory,
  "assets",
  "output",
  "pdf",
  "voltaire-divine-rank-1.pdf",
);
const requiredFiles = [
  htmlPath,
  cssPath,
  join(sourcebookDirectory, "README.md"),
  join(sourcebookDirectory, "voltaire-source-ledger.md"),
  join(sourcebookDirectory, "assets", "scripts", "sourcebook.js"),
  join(sourcebookDirectory, "assets", "scripts", "build-pdf.mjs"),
  join(
    sourcebookDirectory,
    "assets",
    "scripts",
    "build_machinations_dossiers.py",
  ),
];

const failures = [];

for (const requiredFile of requiredFiles) {
  if (!existsSync(requiredFile)) {
    failures.push(`Missing required file: ${requiredFile}`);
  }
}

if (failures.length === 0) {
  const html = readFileSync(htmlPath, "utf8");
  const css = readFileSync(cssPath, "utf8");
  const folios = [...html.matchAll(/data-folio="(\d+)"/g)].map(
    (match) => Number(match[1]),
  );
  const expectedFolios = Array.from({ length: 16 }, (_, index) => index + 1);

  if (JSON.stringify(folios) !== JSON.stringify(expectedFolios)) {
    failures.push(
      `Expected folios 1-16 in order; found: ${folios.join(", ") || "none"}`,
    );
  }

  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);
  const duplicateIds = ids.filter((id, index) => ids.indexOf(id) !== index);

  if (duplicateIds.length > 0) {
    failures.push(`Duplicate HTML ids: ${[...new Set(duplicateIds)].join(", ")}`);
  }

  for (const match of html.matchAll(/<img\b[^>]*>/g)) {
    const imageTag = match[0];
    const src = imageTag.match(/\ssrc="([^"]+)"/)?.[1];
    const alt = imageTag.match(/\salt="([^"]*)"/)?.[1];

    if (!src) {
      failures.push(`Image without src: ${imageTag}`);
      continue;
    }

    if (alt === undefined || alt.trim() === "") {
      failures.push(`Image without meaningful alt text: ${src}`);
    }

    const imagePath = resolve(sourcebookDirectory, src);
    if (!existsSync(imagePath)) {
      failures.push(`Referenced image does not exist: ${src}`);
    }
  }

  for (const match of html.matchAll(/href="#([^"]+)"/g)) {
    const target = match[1];
    if (!ids.includes(target)) {
      failures.push(`Internal link target does not exist: #${target}`);
    }
  }

  const placeholderPattern =
    /\b(TODO|TBD|lorem ipsum|insert lore|placeholder text)\b/i;
  if (placeholderPattern.test(html)) {
    failures.push("Placeholder language remains in index.html.");
  }

  if (/https?:\/\//i.test(html) || /@import\s+url/i.test(css)) {
    failures.push("The local dossier contains an external web dependency.");
  }

  if (!/@page\s*\{[^}]*size:\s*A4/is.test(css)) {
    failures.push("Print CSS does not declare A4 page size.");
  }

  if (!/print-color-adjust:\s*exact/i.test(css)) {
    failures.push("Print CSS does not preserve background colours.");
  }
}

if (existsSync(pdfPath)) {
  const pdfSize = statSync(pdfPath).size;

  if (pdfSize < 100_000) {
    failures.push("The PDF exists but is unexpectedly small.");
  }

  if (pdfSize > 10 * 1024 * 1024) {
    failures.push(
      "The PDF exceeds 10 MiB; install/configure Ghostscript and rebuild the compact print edition.",
    );
  }
}

if (failures.length > 0) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log("Sourcebook structure, links, assets, and print hooks are valid.");
