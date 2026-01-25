---
name: pdf-to-md
description: Convert PDFs in a folder to Markdown and extract embedded images (including JPEG2000 -> PNG) using pypdf.
---

# PDF → Markdown (and Images)

Use this skill to convert campaign PDFs (character sheets, session exports, handouts) into Obsidian-friendly Markdown, optionally extracting embedded images into a sibling folder.

## Quickstart

Convert a single PDF:
- `python3 .codex/skills/pdf-to-md/scripts/pdf_to_md.py --root "Voltaire/Character Sheets" --force`

Convert all PDFs under `Adventures/`:
- `python3 .codex/skills/pdf-to-md/scripts/pdf_to_md.py --root Adventures --force`

## Behavior

- Writes `<pdf>.md` next to the PDF.
- Extracts embedded images into a folder named after the PDF (e.g. `Foo.pdf` → `Foo/`).
- Converts embedded JPEG2000 (`.jp2`) images to `.png` when possible (Pillow).

