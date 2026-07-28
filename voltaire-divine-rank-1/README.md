# Voltaire — Divine Rank 1 Sourcebook

This directory contains a self-contained, sixteen-page sourcebook dossier for Voltaire at Divine Rank 1. It is designed for local reading and repeatable A4 PDF generation without a web server or external web assets.

## Contents

- `index.html` — the complete, accessible sourcebook.
- `styles.css` — screen, responsive, and A4 print styling.
- `assets/` — local artwork used by the dossier.
- `scripts/sourcebook.js` — the print control and single-folio preview helper.
- `scripts/verify-sourcebook.mjs` — structural, link, asset, accessibility, and print-hook checks.
- `scripts/build-pdf.mjs` — headless Chrome/Edge PDF generation.
- `voltaire-source-ledger.md` — an auditable map from major claims to repository evidence and confidence classifications.
- `voltaire-divine-rank-1.pdf` — the generated print edition.

## Read locally

Open `index.html` directly in Chrome, Edge, Firefox, or another modern browser. Double-clicking the file is sufficient; no local server or installation step is required.

For visual review of one printed page, append `?folio=1` to the local URL, replacing `1` with any folio from `1` through `16`:

```text
file:///path/to/voltaire-divine-rank-1/index.html?folio=1
```

The query hides every other folio for screen review only. Remove it to restore the complete dossier. The PDF builder always renders the full document.

## Prerequisites

- Node.js 18 or newer.
- Google Chrome or Microsoft Edge.
- Ghostscript 10 or newer for the compact print edition (recommended).

The scripts use Node's built-in modules, so there is no package install step.
Without Ghostscript, the builder still creates a valid browser PDF, but it will
be substantially larger and will not pass the dossier's 10 MiB archive-size
check.

## Verify and regenerate

Run these commands from the `voltaire-divine-rank-1` directory:

```powershell
node scripts/verify-sourcebook.mjs
node scripts/build-pdf.mjs
```

The verifier checks required files, folio order, duplicate IDs, internal links, image files and alt text, placeholder language, external dependencies, and essential A4 print rules.

The build command writes `voltaire-divine-rank-1.pdf` beside `index.html`. It uses a temporary browser profile, includes print backgrounds, suppresses browser headers and footers, and requests a PDF document outline. When Ghostscript is available, the builder then applies the tested 240 dpi print profile, reducing the PDF to roughly 6 MiB while retaining vector text, page geometry, backgrounds, and print-quality artwork.

The builder searches common Chrome and Edge locations. To use a different executable, set `VOLTAIRE_CHROME_PATH` before running it:

```powershell
$env:VOLTAIRE_CHROME_PATH = "C:\Path\To\chrome.exe"
node scripts/build-pdf.mjs
```

The builder searches the usual Ghostscript installation directory and `PATH`.
To use a portable or non-standard installation:

```powershell
$env:VOLTAIRE_GHOSTSCRIPT_PATH = "C:\Path\To\gswin64c.exe"
node scripts/build-pdf.mjs
```

On macOS or Linux:

```sh
VOLTAIRE_CHROME_PATH="/path/to/chrome" \
VOLTAIRE_GHOSTSCRIPT_PATH="/path/to/gs" \
node scripts/build-pdf.mjs
```

## Accessibility and print

The HTML is the primary accessible edition. Preserve its semantic headings, table structure, descriptive image alternatives, captions, keyboard-operable controls, and readable contrast when making changes.

The stylesheet fixes each folio to A4, preserves background colours, and controls page breaks. After any content or layout change:

1. Run the verifier.
2. Review affected pages with `?folio=1`, changing the folio number as needed.
3. Regenerate the PDF.
4. Inspect the PDF visually for clipped text, overflow, blank pages, split panels, illegible captions, and missing backgrounds.

For manual printing from the browser, use A4 paper, 100% or “Actual size,” background graphics enabled, and browser headers and footers disabled.

## Provenance and canon

The dossier treats the Voltaire repository as its primary lore source. The source ledger distinguishes explicit canon, strong inference, weak inference, artistic framing, and unresolved contradiction. It also preserves Party, Voltaire-only, and DM-private knowledge boundaries.

Artwork was sourced from the repository. Opaque PNG presentation copies were mechanically re-encoded as high-quality JPEGs to keep the local HTML and generated PDF practical; the conversion did not resize, crop, retouch, or otherwise alter their content. The two handwritten JPEG photographs remain byte-identical copies. Much of the artwork appears to have been produced through the project's OpenAI image-generation workflow, but individual files do not consistently retain generation or licensing metadata. Consult the source ledger before redistributing artwork, and do not infer third-party licensing from inclusion in this dossier.

## Maintenance

- Update `voltaire-source-ledger.md` whenever a major claim, quotation, relationship, mechanic, or interpretation changes. Include source paths and useful headings, dates, or line ranges.
- Keep every claim's classification current. Do not silently promote speculation, artistic reconstruction, prospective ritual material, or DM-private planning into confirmed canon.
- Reconcile mechanics against the newest dated D&D Beyond snapshot rather than older summaries.
- Keep assets local, add meaningful alt text, and avoid external font, script, or image dependencies.
- Preserve `data-folio` numbering. If the intended page count changes, update the verifier's expected folio sequence deliberately.
- Regenerate and visually inspect the PDF after every material HTML, CSS, script, asset, or lore revision.
