#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


def _clean_extracted_text(text: str) -> str:
    # Keep layout-ish text but avoid huge blank stretches and trailing whitespace noise.
    normalized = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    out: list[str] = []
    blank_run = 0
    for line in lines:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                out.append("")
            continue
        blank_run = 0
        out.append(line)
    return "\n".join(out).strip()


def _sniff_image_extension(data: bytes) -> str | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"GIF87a") or data.startswith(b"GIF89a"):
        return ".gif"
    if data.startswith(b"BM"):
        return ".bmp"
    if data.startswith(b"II*\x00") or data.startswith(b"MM\x00*"):
        return ".tiff"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return ".webp"
    if data.startswith(b"\x00\x00\x00\x0cjP  \r\n\x87\n"):
        return ".jp2"
    return None


def _normalize_extension(extension: str) -> str:
    ext = extension.strip().lower()
    if not ext:
        return ""
    if ext in {"jpeg", "jpe"}:
        ext = "jpg"
    if ext in {"tif"}:
        ext = "tiff"
    if ext in {"jp2k", "jpx", "jpf"}:
        ext = "jp2"
    if not ext.startswith("."):
        ext = f".{ext}"
    return ext


def convert_pdf_to_markdown(pdf_path: Path, *, force: bool, extract_images: bool) -> str:
    md_path = pdf_path.with_suffix(".md")
    if md_path.exists() and not force:
        return "skipped (md exists)"

    reader = PdfReader(str(pdf_path))
    image_dir = pdf_path.with_suffix("")  # e.g. Adventures/foo.pdf -> Adventures/foo/
    wrote_any_images = False

    if force and extract_images and image_dir.exists() and image_dir.is_dir():
        for existing in image_dir.glob("page-???-img-??.*"):
            try:
                existing.unlink()
            except OSError:
                pass

    md_lines: list[str] = []
    md_lines.append(f"# {pdf_path.stem}")
    md_lines.append("")
    md_lines.append(f"_Source: `{pdf_path.name}`_")
    md_lines.append("")
    md_lines.append(f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_")
    md_lines.append("")

    for page_number, page in enumerate(reader.pages, start=1):
        md_lines.append(f"## Page {page_number}")
        md_lines.append("")

        extracted_text = page.extract_text() or ""
        extracted_text = _clean_extracted_text(extracted_text)
        if extracted_text:
            md_lines.append(extracted_text)
        else:
            md_lines.append("_No extractable text found on this page._")
        md_lines.append("")

        if not extract_images:
            continue

        page_image_filenames: list[str] = []
        if hasattr(page, "images"):
            # pypdf >= 3.10 exposes a convenient `page.images` list.
            for img_index, img in enumerate(page.images, start=1):
                data = getattr(img, "data", None)
                if not data:
                    continue

                extension = _normalize_extension(getattr(img, "extension", "") or "")
                if not extension or extension == ".bin":
                    extension = _sniff_image_extension(data) or ".bin"

                filename = f"page-{page_number:03d}-img-{img_index:02d}{extension}"
                if not wrote_any_images:
                    image_dir.mkdir(parents=True, exist_ok=True)
                    wrote_any_images = True

                (image_dir / filename).write_bytes(data)
                page_image_filenames.append(filename)

        if page_image_filenames:
            md_lines.append("### Images")
            md_lines.append("")
            for filename in page_image_filenames:
                md_lines.append(f"![](./{image_dir.name}/{filename})")
                md_lines.append("")

    md_path.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")
    return "converted"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Convert PDFs to Markdown (and extract images) using pypdf.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("Adventures"),
        help="Directory to scan for PDFs (default: Adventures)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing .md files if present",
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Do not extract embedded images",
    )
    args = parser.parse_args(argv)

    root: Path = args.root
    if not root.exists():
        print(f"error: root not found: {root}", file=sys.stderr)
        return 2

    pdf_paths = sorted(p for p in root.rglob("*.pdf") if p.is_file())
    if not pdf_paths:
        print(f"No PDFs found under {root}")
        return 0

    failures = 0
    for pdf_path in pdf_paths:
        try:
            status = convert_pdf_to_markdown(pdf_path, force=args.force, extract_images=not args.no_images)
            print(f"{pdf_path}: {status}")
        except Exception as exc:
            failures += 1
            print(f"{pdf_path}: failed ({exc.__class__.__name__}: {exc})", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
