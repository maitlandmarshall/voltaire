"""Build the two illustrated Machinations & Actions character dossiers."""

from __future__ import annotations

import io
import math
import random
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
SOURCEBOOK_DIRECTORY = SCRIPT_DIRECTORY.parents[1]


def find_repository_root(start: Path) -> Path:
    """Find the campaign repository without coupling the project to its depth."""

    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate

    raise RuntimeError(f"Could not find the repository root above {start}")


ROOT = find_repository_root(SOURCEBOOK_DIRECTORY)
OUTPUT_DIR = SOURCEBOOK_DIRECTORY / "assets" / "output" / "pdf"
PLATE_DIR = OUTPUT_DIR / "plates"

PAGE_WIDTH, PAGE_HEIGHT = A4
MAIN_LEFT = 17 * mm
MAIN_RIGHT = 158 * mm
MARGIN_LEFT = 166 * mm
MARGIN_RIGHT = 199 * mm
TOP = PAGE_HEIGHT - 20 * mm
BOTTOM = 17 * mm

INK = colors.HexColor("#21170f")
SOFT_INK = colors.HexColor("#4a3424")
PARCHMENT = colors.HexColor("#e7d0a0")
LIGHT_PARCHMENT = colors.HexColor("#f3e4bf")
DARK_PARCHMENT = colors.HexColor("#b9935e")
GOLD = colors.HexColor("#b57b24")
BRIGHT_GOLD = colors.HexColor("#e0ad45")
DRIED_BLOOD = colors.HexColor("#6f251d")
SHADOW_PURPLE = colors.HexColor("#35243d")
MUTED_GREEN = colors.HexColor("#405443")


def register_fonts() -> None:
    """Use dependable Windows fonts while keeping the dossier handwritten."""

    font_dir = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont("Book", str(font_dir / "georgia.ttf")))
    pdfmetrics.registerFont(TTFont("Book-Bold", str(font_dir / "georgiab.ttf")))
    pdfmetrics.registerFont(TTFont("Book-Italic", str(font_dir / "georgiai.ttf")))
    pdfmetrics.registerFont(TTFont("Book-BoldItalic", str(font_dir / "georgiaz.ttf")))
    pdfmetrics.registerFont(TTFont("Scribble", str(font_dir / "segoesc.ttf")))
    pdfmetrics.registerFont(TTFont("Scribble-Bold", str(font_dir / "segoescb.ttf")))


BODY = ParagraphStyle(
    "body",
    fontName="Book",
    fontSize=9.1,
    leading=12.1,
    textColor=INK,
    spaceAfter=4,
)
BODY_SMALL = ParagraphStyle(
    "body-small",
    parent=BODY,
    fontSize=7.8,
    leading=10.1,
)
BODY_TINY = ParagraphStyle(
    "body-tiny",
    parent=BODY,
    fontSize=6.8,
    leading=8.4,
)
QUOTE = ParagraphStyle(
    "quote",
    parent=BODY,
    fontName="Book-Italic",
    fontSize=10.5,
    leading=14,
    leftIndent=12,
    rightIndent=8,
    textColor=SHADOW_PURPLE,
)
CENTERED = ParagraphStyle(
    "centered",
    parent=BODY,
    alignment=TA_CENTER,
)
BOX_HEADING = ParagraphStyle(
    "box-heading",
    parent=BODY,
    fontName="Book-Bold",
    fontSize=10.5,
    leading=13,
    textColor=DRIED_BLOOD,
)
LABEL = ParagraphStyle(
    "label",
    parent=BODY,
    fontName="Book-Bold",
    fontSize=7.2,
    leading=8.5,
    textColor=SOFT_INK,
)


def paragraph_height(text: str, width: float, style: ParagraphStyle = BODY) -> float:
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    return height


def draw_paragraph(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    top: float,
    width: float,
    style: ParagraphStyle = BODY,
) -> float:
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top - height)
    return top - height


def draw_parchment(pdf: canvas.Canvas, seed: int, folio: int, running_title: str) -> None:
    """Lay down a deterministic stained parchment with stitched-hide edges."""

    rng = random.Random(seed)
    pdf.setFillColor(PARCHMENT)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Broad stains stay close to the parchment value so they read as age, not polka dots.
    for _ in range(8):
        pdf.setFillColor(rng.choice([colors.HexColor("#dfc58f"), colors.HexColor("#ead7aa")]))
        radius = rng.uniform(12, 30) * mm
        pdf.circle(
            rng.uniform(0, PAGE_WIDTH),
            rng.uniform(0, PAGE_HEIGHT),
            radius,
            fill=1,
            stroke=0,
        )

    # Dense tiny flecks add tooth without competing with text.
    for _ in range(130):
        pdf.setFillColor(rng.choice([colors.HexColor("#cfae72"), colors.HexColor("#dec28c")]))
        radius = rng.uniform(0.2, 1.1) * mm
        pdf.circle(
            rng.uniform(8 * mm, PAGE_WIDTH - 8 * mm),
            rng.uniform(8 * mm, PAGE_HEIGHT - 8 * mm),
            radius,
            fill=1,
            stroke=0,
        )

    pdf.setFillColor(colors.HexColor("#d9bd84"))
    pdf.setFont("Book-Bold", 170)
    pdf.drawCentredString(PAGE_WIDTH / 2 - 10 * mm, 28 * mm, "V")

    pdf.setStrokeColor(INK)
    pdf.setLineWidth(1.2)
    pdf.rect(8 * mm, 8 * mm, PAGE_WIDTH - 16 * mm, PAGE_HEIGHT - 16 * mm)
    pdf.setStrokeColor(DRIED_BLOOD)
    pdf.setLineWidth(0.5)
    pdf.rect(10.5 * mm, 10.5 * mm, PAGE_WIDTH - 21 * mm, PAGE_HEIGHT - 21 * mm)

    # Short angled stitches make the page feel bound in patched hide.
    pdf.setStrokeColor(SOFT_INK)
    for y in range(int(15 * mm), int(PAGE_HEIGHT - 15 * mm), int(9 * mm)):
        pdf.line(8 * mm, y, 10.5 * mm, y + 2 * mm)
        pdf.line(PAGE_WIDTH - 10.5 * mm, y, PAGE_WIDTH - 8 * mm, y + 2 * mm)

    pdf.setStrokeColor(SHADOW_PURPLE)
    pdf.setLineWidth(0.45)
    pdf.line(162 * mm, BOTTOM, 162 * mm, TOP + 3 * mm)

    pdf.setFillColor(SOFT_INK)
    pdf.setFont("Book-Italic", 6.8)
    pdf.drawString(MAIN_LEFT, 10.5 * mm, running_title)
    pdf.drawRightString(PAGE_WIDTH - 12 * mm, 10.5 * mm, f"leaf {folio}")


def draw_running_header(pdf: canvas.Canvas, kicker: str, title: str) -> float:
    pdf.setFillColor(DRIED_BLOOD)
    pdf.setFont("Book-Bold", 7.5)
    pdf.drawString(MAIN_LEFT, TOP + 3 * mm, kicker.upper())

    pdf.setFillColor(INK)
    title_size = 21.0
    available_width = MAIN_RIGHT - MAIN_LEFT
    while pdfmetrics.stringWidth(title, "Book-Bold", title_size) > available_width and title_size > 13.5:
        title_size -= 0.5
    pdf.setFont("Book-Bold", title_size)
    pdf.drawString(MAIN_LEFT, TOP - 5 * mm, title)

    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(1.1)
    pdf.line(MAIN_LEFT, TOP - 8 * mm, MAIN_RIGHT, TOP - 8 * mm)
    return TOP - 14 * mm


def draw_marginalia(
    pdf: canvas.Canvas,
    notes: list[tuple[float, str, colors.Color, float]],
) -> None:
    """Write notes into the narrow outer margin at supplied top positions."""

    width = MARGIN_RIGHT - MARGIN_LEFT - 3 * mm
    for top, text, color, angle in notes:
        words = text.split()
        lines: list[str] = []
        current = ""

        for word in words:
            candidate = f"{current} {word}".strip()
            if pdfmetrics.stringWidth(candidate, "Scribble", 7.1) <= width:
                current = candidate
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)

        pdf.saveState()
        pdf.translate(MARGIN_LEFT, top)
        pdf.rotate(angle)
        pdf.setFillColor(color)
        pdf.setFont("Scribble", 7.1)
        baseline = 0
        for line in lines:
            pdf.drawString(0, baseline, line)
            baseline -= 9
        pdf.restoreState()


def cropped_reader(path: Path, target_width: float, target_height: float) -> object:
    """Crop an image to the requested frame without creating extra files."""

    with Image.open(path) as source:
        source = source.convert("RGB")
        target_ratio = target_width / target_height
        source_ratio = source.width / source.height

        if source_ratio > target_ratio:
            crop_width = int(source.height * target_ratio)
            left = (source.width - crop_width) // 2
            crop = source.crop((left, 0, left + crop_width, source.height))
        else:
            crop_height = int(source.width / target_ratio)
            top = (source.height - crop_height) // 2
            crop = source.crop((0, top, source.width, top + crop_height))

        crop = crop.resize((max(1, int(target_width * 2)), max(1, int(target_height * 2))))
        buffer = io.BytesIO()
        crop.save(buffer, format="JPEG", quality=92)
        buffer.seek(0)
        return buffer


def draw_image(
    pdf: canvas.Canvas,
    path: Path,
    x: float,
    y: float,
    width: float,
    height: float,
    caption: str | None = None,
) -> None:
    buffer = cropped_reader(path, width, height)
    pdf.drawImage(ImageReader(buffer), x, y, width, height, preserveAspectRatio=False, mask="auto")
    pdf.setStrokeColor(INK)
    pdf.setLineWidth(0.7)
    pdf.rect(x, y, width, height, fill=0, stroke=1)

    if caption:
        caption_style = ParagraphStyle(
            "caption",
            fontName="Book-Italic",
            fontSize=5.8,
            leading=6.6,
            textColor=INK,
            alignment=TA_CENTER,
        )
        draw_paragraph(pdf, caption, x, y - 3, width, caption_style)


def draw_image_fit(
    pdf: canvas.Canvas,
    path: Path,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None:
    """Fit an image inside a frame without cropping it."""

    with Image.open(path) as source:
        source = source.convert("RGB")
        fitted = ImageOps.contain(source, (int(width * 2), int(height * 2)))
        fitted = ImageEnhance.Contrast(fitted).enhance(1.03)

        background = Image.new("RGB", (int(width * 2), int(height * 2)), (33, 23, 15))
        left = (background.width - fitted.width) // 2
        top = (background.height - fitted.height) // 2
        background.paste(fitted, (left, top))

        buffer = io.BytesIO()
        background.save(buffer, format="JPEG", quality=93)
        buffer.seek(0)

    pdf.drawImage(ImageReader(buffer), x, y, width, height, preserveAspectRatio=False)
    pdf.setStrokeColor(INK)
    pdf.rect(x, y, width, height, fill=0, stroke=1)


def draw_box(
    pdf: canvas.Canvas,
    x: float,
    top: float,
    width: float,
    title: str,
    paragraphs: list[str],
    *,
    style: ParagraphStyle = BODY,
    fill: colors.Color = LIGHT_PARCHMENT,
    padding: float = 7,
) -> float:
    inner_width = width - 2 * padding
    title_height = paragraph_height(title, inner_width, BOX_HEADING)
    body_heights = [paragraph_height(text, inner_width, style) for text in paragraphs]
    box_height = padding * 2 + title_height + 4 + sum(body_heights) + max(0, len(paragraphs) - 1) * 3

    pdf.saveState()
    pdf.setFillAlpha(0.78)
    pdf.setFillColor(fill)
    pdf.roundRect(x, top - box_height, width, box_height, 5, fill=1, stroke=0)
    pdf.restoreState()
    pdf.setStrokeColor(SOFT_INK)
    pdf.setLineWidth(0.6)
    pdf.roundRect(x, top - box_height, width, box_height, 5, fill=0, stroke=1)

    cursor = top - padding
    cursor = draw_paragraph(pdf, title, x + padding, cursor, inner_width, BOX_HEADING) - 4
    for text in paragraphs:
        cursor = draw_paragraph(pdf, text, x + padding, cursor, inner_width, style) - 3

    return top - box_height


def draw_table(
    pdf: canvas.Canvas,
    data: list[list[str]],
    x: float,
    top: float,
    widths: list[float],
    *,
    font_size: float = 7.1,
    row_padding: float = 3.2,
) -> float:
    header_style = ParagraphStyle(
        "table-header",
        fontName="Book-Bold",
        fontSize=font_size,
        leading=font_size + 1.4,
        textColor=colors.HexColor("#f4dfb1"),
        alignment=TA_LEFT,
    )
    cell_style = ParagraphStyle(
        "table-cell",
        fontName="Book",
        fontSize=font_size,
        leading=font_size + 1.6,
        textColor=INK,
        alignment=TA_LEFT,
    )
    wrapped_data = [
        [Paragraph(str(value), header_style if row_index == 0 else cell_style) for value in row]
        for row_index, row in enumerate(data)
    ]
    table = Table(wrapped_data, colWidths=widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), SHADOW_PURPLE),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_PARCHMENT, PARCHMENT]),
                ("GRID", (0, 0), (-1, -1), 0.35, SOFT_INK),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), row_padding),
                ("BOTTOMPADDING", (0, 0), (-1, -1), row_padding),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    _, height = table.wrap(sum(widths), PAGE_HEIGHT)
    table.drawOn(pdf, x, top - height)
    return top - height


def draw_stat_seals(pdf: canvas.Canvas, stats: list[tuple[str, int, str]], top: float) -> float:
    width = MAIN_RIGHT - MAIN_LEFT
    spacing = width / len(stats)
    radius = 13 * mm

    for index, (name, value, modifier) in enumerate(stats):
        center_x = MAIN_LEFT + spacing * (index + 0.5)
        center_y = top - radius
        pdf.setFillColor(colors.HexColor("#d7bb80"))
        pdf.setStrokeColor(SHADOW_PURPLE)
        pdf.setLineWidth(1)
        pdf.circle(center_x, center_y, radius, fill=1, stroke=1)
        pdf.setFillColor(SOFT_INK)
        pdf.setFont("Book-Bold", 6.2)
        pdf.drawCentredString(center_x, center_y + 13, name)
        pdf.setFont("Book-Bold", 16)
        pdf.drawCentredString(center_x, center_y - 4, str(value))
        pdf.setFont("Book-Italic", 7)
        pdf.drawCentredString(center_x, center_y - 15, modifier)

    return top - 2 * radius - 4 * mm


def draw_cover(
    pdf: canvas.Canvas,
    image_path: Path,
    title: str,
    subtitle: str,
    subject: str,
    seal: str,
) -> None:
    draw_image(pdf, image_path, 0, 0, PAGE_WIDTH, PAGE_HEIGHT)

    pdf.saveState()
    pdf.setFillAlpha(0.76)
    pdf.setFillColor(colors.black)
    pdf.roundRect(16 * mm, PAGE_HEIGHT - 72 * mm, PAGE_WIDTH - 32 * mm, 50 * mm, 8, fill=1, stroke=0)
    pdf.roundRect(20 * mm, 18 * mm, PAGE_WIDTH - 40 * mm, 47 * mm, 8, fill=1, stroke=0)
    pdf.restoreState()

    pdf.setFillColor(BRIGHT_GOLD)
    pdf.setFont("Book-Bold", 23)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 36 * mm, title)
    pdf.setFont("Book-Italic", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 46 * mm, subtitle)

    pdf.setFillColor(colors.HexColor("#f2dfb4"))
    pdf.setFont("Book-Bold", 27)
    pdf.drawCentredString(PAGE_WIDTH / 2, 48 * mm, subject)
    pdf.setFont("Scribble", 9)
    pdf.drawCentredString(PAGE_WIDTH / 2, 35 * mm, seal)

    pdf.setStrokeColor(BRIGHT_GOLD)
    pdf.setLineWidth(1)
    pdf.rect(8 * mm, 8 * mm, PAGE_WIDTH - 16 * mm, PAGE_HEIGHT - 16 * mm)
    pdf.showPage()


def voltaire_pdf() -> Path:
    output_path = OUTPUT_DIR / "Voltaire_First_Divine_Dossier.pdf"
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1)
    pdf.setTitle("Voltaire the Black - First Divine Dossier")
    pdf.setAuthor("Voltaire the Black, catalogued in Machinations & Actions: 5e")
    pdf.setSubject("In-world D&D character dossier")

    draw_cover(
        pdf,
        PLATE_DIR / "voltaire_divine_dossier_plate.png",
        "MACHINATIONS & ACTIONS: 5e",
        "First Divine Dossier - Catalogue of the Author",
        "VOLTAIRE THE BLACK",
        "Recorded by the subject, who is also the patron, witness, and jurisdiction.",
    )

    # Leaf I - declaration and physical census.
    draw_parchment(pdf, 101, 1, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article I", "Declaration of Subject")
    draw_image(
        pdf,
        ROOT / "Codex/Characters/Party/Voltaire_portrait.png",
        MAIN_RIGHT - 52 * mm,
        cursor - 52 * mm,
        52 * mm,
        52 * mm,
        "The face habitually worn by the author.",
    )
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT - 58 * mm,
        "I, Voltaire, catalogue myself.",
        [
            "This is the first dossier of my declared divinity. It is written in the first person because all honest scripture eventually is.",
            "<b>Status:</b> living; self-patroned; Divine Rank 1; awaiting formal execution of the First Rite.",
        ],
        style=BODY_SMALL,
    )
    cursor -= 7 * mm
    identity_data = [
        ["ENTRY", "CATALOGUED VALUE"],
        ["Name", "Voltaire the Black"],
        ["Player", "Dicfuc"],
        ["Present species", "Variant Human - formerly a Fae Prince"],
        ["Class", "Rogue 5 (Thief) / Warlock 8 (Archfey)"],
        ["Background", "Hermit"],
        ["Alignment", "Chaotic Neutral"],
        ["Level / Experience", "13 / 122,783 of 140,000 XP"],
        ["Faith", "Self Worship"],
        ["Divine office", "Rank 1; proposed Domain of Unbecoming"],
    ]
    cursor = draw_table(pdf, identity_data, MAIN_LEFT, cursor, [45 * mm, 96 * mm], font_size=7.4)
    cursor -= 6 * mm
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Physical inventory of the god-body",
        [
            "<b>Age:</b> 30. <b>Height:</b> 185 cm (6 ft. 1 in.). <b>Weight:</b> 185 lb before equipment, divine gravitas, or argumentative crab.",
            "<b>Hair:</b> dark. <b>Skin:</b> pale/white, extensively tattooed. <b>Eyes:</b> brown, perpetually open, and inclined to notice red eyes where others report empty space.",
            "The mouth smiles continuously because frowning hurts. A living crab-soul grimoire is grafted to a donkey-like tail. A V has been carved into the chest and forehead by Shadar-kai initiates.",
        ],
        style=BODY_SMALL,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 8 * mm, "If this page blinks, blink back. I cannot.", DRIED_BLOOD, -3),
            (TOP - 55 * mm, "Age is accurate in years, not in recent subjective months.", SHADOW_PURPLE, 2),
            (TOP - 110 * mm, "Alignment: neutral to whom?", MUTED_GREEN, -2),
            (TOP - 158 * mm, "The crab is a co-author when convenient.", DRIED_BLOOD, 3),
            (TOP - 212 * mm, "Do not add a halo. Halos imply overhead.", SHADOW_PURPLE, -4),
        ],
    )
    pdf.showPage()

    # Leaf II - history and apotheosis.
    draw_parchment(pdf, 102, 2, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article II", "A History of Becoming Incorrectly")
    box_width = (MAIN_RIGHT - MAIN_LEFT - 6 * mm) / 2
    left_top = cursor
    right_top = cursor
    left_top = draw_box(
        pdf,
        MAIN_LEFT,
        left_top,
        box_width,
        "I. The Fall",
        [
            "I was Prince of the Swamp until visiting bards mistook the Deck of Many Things for a social activity. The King of Spades and Ace of Clubs cast me into the Michaca desert, changed my Fae nature into humanity, and took most of my memories.",
            "I objected to the desert. The desert did not apologise.",
        ],
        style=BODY_SMALL,
    )
    right_top = draw_box(
        pdf,
        MAIN_LEFT + box_width + 6 * mm,
        right_top,
        box_width,
        "II. The Transcription",
        [
            "Greg accelerated me with a Potion of Haste and had me read the Book of Vile Darkness and the Book of Exalted Deeds. I survived both, transcribed them into a unified work, and learned every language without noticing that I had done so.",
            "Good and evil are therefore reference sections.",
        ],
        style=BODY_SMALL,
    )
    cursor = min(left_top, right_top) - 7 * mm
    draw_image(
        pdf,
        ROOT / "Adventures/2026-07-25/2026-07-25_mask-statue-ritual.png",
        MAIN_LEFT,
        cursor - 68 * mm,
        72 * mm,
        68 * mm,
        "Mask's hollow statue: occupied vacancy, six subjective months.",
    )
    right_cursor = draw_box(
        pdf,
        MAIN_LEFT + 78 * mm,
        cursor,
        MAIN_RIGHT - (MAIN_LEFT + 78 * mm),
        "III. The Sun, the Ink, and the Tail",
        [
            "The Sun Card became both weapon and generative principle. The Ink of Unbeing taught memory to behave like material. My ritual book acquired a crab soul, skins, blood-inks, opinions, and eventually my tail.",
            "Robin emerged when a following frog received the Sun Card and reality rolled well.",
        ],
        style=BODY_SMALL,
    )
    right_cursor -= 5 * mm
    right_cursor = draw_box(
        pdf,
        MAIN_LEFT + 78 * mm,
        right_cursor,
        MAIN_RIGHT - (MAIN_LEFT + 78 * mm),
        "IV. Rank One",
        [
            "Roughly twenty Shadar-kai marked me with V, admitted me to the tower, and dedicated themselves. I destroyed the hollow statue of dethroned Mask, stood in its place, and was recorded as Divine Rank 1.",
            "This is not the end of the argument. It is the first numbered footnote.",
        ],
        style=BODY_SMALL,
    )
    cursor = min(cursor - 75 * mm, right_cursor) - 7 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Two events suitable for official forms",
        [
            "<b>Notable Event One - The Fall from Grace:</b> dispossession, desert exile, human transformation, and loss of the swamp-prince memory.",
            "<b>Notable Event Two - The Ascension of V:</b> Shadar-kai recognition, destruction of Mask's hollow statue, and attainment of Divine Rank 1.",
        ],
        style=BODY_SMALL,
        fill=colors.HexColor("#dbc08a"),
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 12 * mm, "No one warned me that cards were geography.", DRIED_BLOOD, -2),
            (TOP - 75 * mm, "Universal language: the only proficiency with no sensible dropdown.", SHADOW_PURPLE, 3),
            (TOP - 137 * mm, "Mask left a vacancy. I brought posture.", MUTED_GREEN, -4),
            (TOP - 201 * mm, "Twelve subjective months now live between lines.", DRIED_BLOOD, 2),
        ],
    )
    pdf.showPage()

    # Leaf III - numerical proof.
    draw_parchment(pdf, 103, 3, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article III", "Numerical Proof of Existence")
    cursor = draw_stat_seals(
        pdf,
        [
            ("STR", 7, "-2"),
            ("DEX", 19, "+4"),
            ("CON", 16, "+3"),
            ("INT", 19, "+4"),
            ("WIS", 9, "-1"),
            ("CHA", 20, "+5"),
        ],
        cursor,
    )
    cursor -= 4 * mm
    combat_data = [
        ["MEASURE", "VALUE", "ANNOTATION"],
        ["Armour Class", "19", "12 base +4 Dex +2 enhancement +1 Ring"],
        ["Maximum HP", "100", "13d8 total class Hit Dice"],
        ["Initiative", "+4", "Dexterity"],
        ["Speed", "30 ft.", "Climbing costs no extra movement"],
        ["Passive senses", "19 / 9 / 14", "Perception / Insight / Investigation"],
        ["Darkvision", "120 ft.", "Robe-assisted, as recorded"],
        ["Proficiency", "+5", "Level 13"],
        ["Carrying", "105 / 210 / 230 lb.", "Capacity / push-drag-lift / actually carried"],
    ]
    cursor = draw_table(
        pdf,
        combat_data,
        MAIN_LEFT,
        cursor,
        [36 * mm, 29 * mm, 76 * mm],
        font_size=6.9,
    )
    cursor -= 5 * mm
    saves = [
        ["SAVE", "TOTAL", "STATUS"],
        ["Strength", "-1", "Ring +1"],
        ["Dexterity", "+10", "Prof. + Ring"],
        ["Constitution", "+4", "Ring +1"],
        ["Intelligence", "+10", "Prof. + Ring"],
        ["Wisdom", "+0", "Ring +1"],
        ["Charisma", "+6", "Ring +1"],
    ]
    skills = [
        ["SKILL", "MOD", "SKILL", "MOD"],
        ["Acrobatics", "+9", "Animal Handling", "-1"],
        ["Arcana", "+4", "Athletics", "-2"],
        ["Deception", "+5", "History", "+4"],
        ["Insight", "-1", "Intimidation", "+5"],
        ["Investigation", "+4", "Medicine", "+4"],
        ["Nature", "+4", "Perception", "+9"],
        ["Performance", "+10", "Persuasion", "+5"],
        ["Religion", "+9", "Sleight of Hand", "+9"],
        ["Stealth", "+14", "Survival", "-1"],
    ]
    left_width = 55 * mm
    left_bottom = draw_table(pdf, saves, MAIN_LEFT, cursor, [23 * mm, 12 * mm, 20 * mm], font_size=6.2)
    right_bottom = draw_table(
        pdf,
        skills,
        MAIN_LEFT + left_width + 5 * mm,
        cursor,
        [25 * mm, 12 * mm, 25 * mm, 12 * mm],
        font_size=6.0,
    )
    cursor = min(left_bottom, right_bottom) - 5 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Movement curiosities",
        [
            "Running long jump: approximately 11 ft. Running high jump: approximately 5 ft. Second-Story Work supplies the extra 4 ft.; standing jumps are halved. Crawling ordinarily uses half speed.",
        ],
        style=BODY_TINY,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 12 * mm, "Intelligence is 19 because the headband agrees with me.", SHADOW_PURPLE, 2),
            (TOP - 68 * mm, "Performance is +10. Previous scribes were wrong. This is now doctrine.", DRIED_BLOOD, -3),
            (TOP - 130 * mm, "230 lb carried on a 105 lb capacity. Gravity has filed a complaint.", MUTED_GREEN, 4),
            (TOP - 205 * mm, "Wisdom remains economical.", SHADOW_PURPLE, -2),
        ],
    )
    pdf.showPage()

    # Leaf IV - class features and possessions.
    draw_parchment(pdf, 104, 4, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article IV", "Instruments, Advantages, and Other Limbs")
    draw_image_fit(
        pdf,
        ROOT / "Codex/Items/Crab Book/Crab_Book_ref.png",
        MAIN_LEFT,
        cursor - 56 * mm,
        55 * mm,
        55 * mm,
    )
    cursor_right = draw_box(
        pdf,
        MAIN_LEFT + 61 * mm,
        cursor,
        MAIN_RIGHT - (MAIN_LEFT + 61 * mm),
        "The crab-book tail",
        [
            "A sentient ritual grimoire of stitched skins and varied blood-inks, invested with a crab soul and grafted into my tail.",
            "It consumes skin to absorb memories, writes prophecies or lies, and serves as spellbook, companion, archive, and editorial dispute.",
        ],
        style=BODY_SMALL,
    )
    cursor = min(cursor - 62 * mm, cursor_right) - 5 * mm
    features = [
        ["ROGUE / THIEF", "WARLOCK / ARCHFEY"],
        ["Sneak Attack 3d6", "Pact Magic: two 4th-level slots"],
        ["Expertise: Stealth, Perception", "Spell DC 18; attack +10"],
        ["Cunning Action; Steady Aim", "Agonizing Blast"],
        ["Fast Hands; Second-Story Work", "Aspect of the Moon"],
        ["Uncanny Dodge", "Mask of Many Faces"],
        ["Thieves' Cant", "Feral Transformation"],
        ["", "Fey Presence; Misty Escape"],
        ["", "Pact of the Tome"],
    ]
    cursor = draw_table(pdf, features, MAIN_LEFT, cursor, [70.5 * mm, 70.5 * mm], font_size=6.8)
    cursor -= 5 * mm
    equipment = [
        ["BODY / SLOT", "RECORDED IMPLEMENT"],
        ["Head", "Headband of Intellect"],
        ["Garment", "Robe of Eyes"],
        ["Armour", "+2 Studded Leather"],
        ["Shoulders", "Cape of Darkness"],
        ["Finger", "Ring of Protection"],
        ["Hands / weapons", "Two Shadow Daggers +2; Chakram +6; shortbow"],
        ["Additional body part", "Donkey-like tail and living Crab Book"],
        ["Pack", "Thieves' tools, herbalism kit, poles, ropes, light, oil, ball bearings, improbable trophies"],
    ]
    cursor = draw_table(pdf, equipment, MAIN_LEFT, cursor, [42 * mm, 99 * mm], font_size=6.8)
    cursor -= 5 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Feats and trained languages",
        [
            "<b>Feats:</b> Fey Touched; Lucky; Shadow Touched. <b>Armour:</b> light. <b>Weapons:</b> hand crossbow, longsword, rapier, shortsword, simple weapons. <b>Tools:</b> herbalism kit, thieves' tools.",
            "<b>Languages:</b> Abyssal, Common, Elvish, Thieves' Cant, and All. The final entry is neither exaggeration nor sensible.",
        ],
        style=BODY_TINY,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 10 * mm, "The tail counts as an additional body part because forms fear imagination.", DRIED_BLOOD, -3),
            (TOP - 78 * mm, "The Robe has eyes. I have eyes. Management remains contested.", SHADOW_PURPLE, 3),
            (TOP - 150 * mm, "Ball bearings: portable terrain.", MUTED_GREEN, -2),
            (TOP - 215 * mm, "The Sun Card is both equipment and ancestor.", DRIED_BLOOD, 2),
        ],
    )
    pdf.showPage()

    # Leaf V - spells and action economy.
    draw_parchment(pdf, 105, 5, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article V", "Practiced Impossibilities")
    spell_summary = [
        ["PACT MAGIC", "VALUE"],
        ["Spellcasting ability", "Charisma"],
        ["Spell save DC", "18"],
        ["Spell attack", "+10"],
        ["Pact slots", "2 slots, each 4th level"],
        ["At will", "Disguise Self"],
    ]
    draw_image_fit(
        pdf,
        ROOT / "Codex/Items/Sun_Card_ref.png",
        MAIN_RIGHT - 39 * mm,
        cursor - 42 * mm,
        39 * mm,
        39 * mm,
    )
    cursor = draw_table(pdf, spell_summary, MAIN_LEFT, cursor, [38 * mm, 58 * mm], font_size=7.2)
    cursor -= 6 * mm
    spells = [
        ["LEVEL", "SPELLS"],
        ["Cantrips", "Eldritch Blast; Blade Ward; Mage Hand; Guidance; Booming Blade; Word of Radiance"],
        ["1st", "Armor of Agathys; Expeditious Retreat; Hex; Sleep; Silent Image; Disguise Self"],
        ["2nd", "Shadow Blade; Darkness; Suggestion; Misty Step; Invisibility"],
        ["3rd", "Hypnotic Pattern"],
        ["4th", "Greater Invisibility; Summon Greater Demon"],
    ]
    cursor = draw_table(pdf, spells, MAIN_LEFT, cursor, [25 * mm, 116 * mm], font_size=7.1, row_padding=4)
    cursor -= 6 * mm
    left_top = cursor
    right_top = cursor
    left_top = draw_box(
        pdf,
        MAIN_LEFT,
        left_top,
        68 * mm,
        "Favourite buttons",
        [
            "<b>Action:</b> Hypnotic Pattern; Suggestion; Greater Invisibility; Feral Transformation; or the ordinary violence of Eldritch Blast.",
            "<b>Bonus action:</b> Cunning Action; Fast Hands; Misty Step; Shadow Blade; Hex.",
            "<b>Reaction:</b> Uncanny Dodge or Misty Escape.",
        ],
        style=BODY_TINY,
    )
    right_top = draw_box(
        pdf,
        MAIN_LEFT + 74 * mm,
        right_top,
        MAIN_RIGHT - (MAIN_LEFT + 74 * mm),
        "Concentration is singular",
        [
            "Only one of Greater Invisibility, Invisibility, Hypnotic Pattern, Suggestion, Shadow Blade, Hex, Darkness, or Expeditious Retreat may occupy the same thought at once.",
            "Theology contains the same defect.",
        ],
        style=BODY_TINY,
    )
    cursor = min(left_top, right_top) - 6 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Transformations",
        [
            "Once per long rest I may become a dire wolf, giant spider, or giant octopus for up to one hour. I retain Intelligence, Wisdom, Charisma, speech, saving-throw proficiencies, and verbal-only spellcasting. Current state: giant spider, climbing the tower; use expended until recovery.",
        ],
        style=BODY_SMALL,
        fill=colors.HexColor("#d5c18f"),
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 12 * mm, "Two slots. Fourth level. The economy of miracles.", DRIED_BLOOD, 3),
            (TOP - 82 * mm, "Disguise Self is at will. Identity is therefore a wardrobe problem.", SHADOW_PURPLE, -2),
            (TOP - 150 * mm, "Never concentrate on Hex when theatrics are available.", MUTED_GREEN, 2),
            (TOP - 216 * mm, "Octopus remains a theological option.", DRIED_BLOOD, -3),
        ],
    )
    pdf.showPage()

    # Leaf VI - theology and followers.
    draw_parchment(pdf, 106, 6, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article VI", "Theology, Followers, and Jurisdiction")
    draw_image_fit(
        pdf,
        ROOT / "Codex/Factions/Voltaire_followers_sigil.png",
        MAIN_LEFT,
        cursor - 67 * mm,
        67 * mm,
        67 * mm,
    )
    cursor_right = draw_box(
        pdf,
        MAIN_LEFT + 73 * mm,
        cursor,
        MAIN_RIGHT - (MAIN_LEFT + 73 * mm),
        "Religious ideology",
        [
            "Divinity is produced through memory, symbol, recognition, and worship freely directed by independent minds. I worship myself and function as my own patron.",
            "Shar is a formative power and an honoured catalyst. Gratitude does not require subordination.",
            "My emerging sphere is the <b>Domain of Unbecoming</b>: transformation through the destruction of imposed identity.",
        ],
        style=BODY_SMALL,
    )
    cursor = min(cursor - 73 * mm, cursor_right) - 5 * mm
    followers = [
        ["FOLLOWER / BODY", "STATUS"],
        ["Robin", "Disciple; first companion; blessed with V"],
        ["Two Fae specimens", "Memories of prior gods replaced with Voltaire"],
        ["Shrek", "Converted through Ink fine print"],
        ["Blink Dog", "Locally Norhan's; spiritually Voltaire's"],
        ["~20 Shadar-kai", "Confirmed initiates; hierarchy unknown"],
        ["Bloodweb spiders", "Allies or ritual partners; worship unconfirmed"],
    ]
    cursor = draw_table(pdf, followers, MAIN_LEFT, cursor, [50 * mm, 91 * mm], font_size=6.8)
    cursor -= 5 * mm
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "The Followers of V",
        [
            "Provisional organisation-name: <b>The Followers of V</b>. The sigil combines a triangle exceeding a square into a seven-point core, paired eyes, luminous mushroom and hellhound-blood ink, and dark shadowweave filigree.",
            "The mark has been carved into a Shadowfell aspen, where it sank into the bark as though it had always been present. A many-eyed V later manifested remotely within the Temple of Blood.",
        ],
        style=BODY_SMALL,
    )
    cursor -= 5 * mm
    relationships = [
        ["ALLIES / ASSOCIATES", "COMPLICATED OR OPPOSED"],
        ["The party; Robin; Shadar-kai initiates", "Shar - catalyst, rival, not enemy"],
        ["Greg; Glasya; Bloodweb spiders (provisional)", "Corellon - intended confrontation"],
        ["", "Mask - dethroned vacancy; statue destroyed"],
        ["", "Queen of Abeil - hostile authority"],
    ]
    draw_table(pdf, relationships, MAIN_LEFT, cursor, [70.5 * mm, 70.5 * mm], font_size=6.6)
    draw_marginalia(
        pdf,
        [
            (TOP - 10 * mm, "A symbol is a door pretending to be a drawing.", DRIED_BLOOD, -2),
            (TOP - 74 * mm, "Worship that cannot leave is merely furniture.", SHADOW_PURPLE, 3),
            (TOP - 142 * mm, "Shar receives thanks, not ownership.", MUTED_GREEN, -3),
            (TOP - 214 * mm, "Order-name pending. Religions are untidy before stationery.", DRIED_BLOOD, 2),
        ],
    )
    pdf.showPage()

    # Leaf VII - planned rite and unresolved theorem.
    draw_parchment(pdf, 107, 7, "Machinations & Actions: 5e - First Divine Dossier")
    cursor = draw_running_header(pdf, "Article VII - Prospective", "The First Rite, Not Yet Executed")
    draw_image(
        pdf,
        ROOT / "Adventures/2026-07-25/2026-07-25_first-divine-rite_summit-wide.png",
        MAIN_LEFT,
        cursor - 63 * mm,
        68 * mm,
        63 * mm,
        "Prospective plate only: the rite remains unperformed.",
    )
    draw_image(
        pdf,
        ROOT / "Adventures/2026-07-25/2026-07-25_first-divine-rite_network-activation.png",
        MAIN_LEFT + 73 * mm,
        cursor - 63 * mm,
        68 * mm,
        63 * mm,
        "Hypothesis: a network awakened by V through the followers' sigil.",
    )
    cursor -= 73 * mm
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Declared sequence",
        [
            "<b>1.</b> Reach the tower summit and acknowledge my divinity before the gods.",
            "<b>2.</b> Pray to Shar and thank her for her part in my becoming.",
            "<b>3.</b> Cut Shar's circle-square-triangle geometry into my flesh and let the blood fall upon the tower's highest point.",
            "<b>4.</b> Shape the blood into the Followers of V sigil around the anti-light, then drive V through the design.",
            "<b>5.</b> Call every connected sigil already placed.",
        ],
        style=BODY_SMALL,
        fill=colors.HexColor("#d5b37b"),
    )
    cursor -= 5 * mm
    goals = [
        ["PETITION", "INTENDED RESULT"],
        ["Claim", "Transform the tower into Voltaire's realm: a threshold between the Feywild and Shar's realm."],
        ["Connection", "Awaken teleportation between qualified V sigils."],
    ]
    cursor = draw_table(pdf, goals, MAIN_LEFT, cursor, [31 * mm, 110 * mm], font_size=7)
    cursor -= 5 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Unresolved theorems for Lachlan",
        [
            "The blood cost, checks, divine witnesses, Shar's response, network limits, permitted travellers, failure state, and precise mechanics of Divine Rank 1 remain unconfirmed.",
            "The Temple of Blood has already manifested many eyes and V at a distance. Whether that event created the first shrine, a claim, or a network anchor is also unresolved.",
        ],
        style=BODY_SMALL,
        fill=colors.HexColor("#d9c9a1"),
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 9 * mm, "PROSPECTIVE. Do not mistake intention for completed miracle.", DRIED_BLOOD, -3),
            (TOP - 87 * mm, "Blood is ink that insists on provenance.", SHADOW_PURPLE, 2),
            (TOP - 155 * mm, "If every mark becomes a door, remember which side has spiders.", MUTED_GREEN, -2),
            (TOP - 218 * mm, "The rite begins when the table says it begins.", DRIED_BLOOD, 3),
        ],
    )
    pdf.showPage()
    pdf.save()
    return output_path


def robin_pdf() -> Path:
    output_path = OUTPUT_DIR / "Robin_First_Disciple_Dossier.pdf"
    pdf = canvas.Canvas(str(output_path), pagesize=A4, pageCompression=1)
    pdf.setTitle("Robin - First Disciple Dossier")
    pdf.setAuthor("Voltaire the Black, catalogued in Machinations & Actions: 5e")
    pdf.setSubject("In-world D&D companion dossier")

    draw_cover(
        pdf,
        PLATE_DIR / "robin_blessed_dossier_plate.png",
        "MACHINATIONS & ACTIONS: 5e",
        "Companion Leaf - First Disciple Dossier",
        "ROBIN",
        "My sun in the darkness; not a familiar; presently impossible to classify.",
    )

    # Leaf I - identity and origin.
    draw_parchment(pdf, 201, 1, "Machinations & Actions: 5e - Robin, First Disciple")
    cursor = draw_running_header(pdf, "Companion Article I", "Robin, Who Is Not a Familiar")
    draw_image_fit(
        pdf,
        ROOT / "Codex/Characters/Robin_portrait.png",
        MAIN_RIGHT - 55 * mm,
        cursor - 55 * mm,
        55 * mm,
        55 * mm,
    )
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT - 61 * mm,
        "Declaration of independence",
        [
            "Robin is my disciple and companion. She is not equipment, not a pet, and - according to her own immediate and persuasive objection - not an animal.",
            "Any form that lists her under 'familiar' has mistaken proximity for ownership.",
        ],
        style=BODY_SMALL,
    )
    cursor -= 7 * mm
    identity = [
        ["ENTRY", "CATALOGUED VALUE"],
        ["Name", "Robin"],
        ["Affiliation", "Independent disciple and companion of Voltaire"],
        ["Pronouns", "she / her"],
        ["Apparent form", "Shoulder-sized luminous avian-fey with translucent wings"],
        ["Origin", "Frog or toad merged with the Sun Card on a Natural 20"],
        ["Creature type / race", "UNRESOLVED"],
        ["Age / height / weight", "UNRESOLVED"],
        ["Current distinction", "Recipient of the Blessing of V"],
    ]
    cursor = draw_table(pdf, identity, MAIN_LEFT, cursor, [43 * mm, 98 * mm], font_size=7.1)
    cursor -= 6 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Origin, as witnessed by me",
        [
            "A frog or toad had been following me. I flourished the Sun Card and put it into the creature's mouth. White radiance overtook both card and amphibian; they merged and reformed as Robin.",
            "This was not an experiment that failed upward. It was an experiment that arrived.",
        ],
        style=BODY_SMALL,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 8 * mm, "NOT A FAMILIAR.", DRIED_BLOOD, -4),
            (TOP - 58 * mm, "The frog had excellent judgement.", MUTED_GREEN, 2),
            (TOP - 118 * mm, "Natural 20: reality signed the birth record.", SHADOW_PURPLE, -2),
            (TOP - 177 * mm, "Do not put her in a component pouch.", DRIED_BLOOD, 3),
            (TOP - 222 * mm, "Classification may follow consent.", MUTED_GREEN, -3),
        ],
    )
    pdf.showPage()

    # Leaf II - conduct and history.
    draw_parchment(pdf, 202, 2, "Machinations & Actions: 5e - Robin, First Disciple")
    cursor = draw_running_header(pdf, "Companion Article II", "Observed Conduct and Layered Geography")
    panel_width = 44 * mm
    image_y = cursor - 44 * mm
    draw_image(
        pdf,
        ROOT / "Adventures/2026-01-25/2026-01-25_robin-shoulder-dialogue_wide.png",
        MAIN_LEFT,
        image_y,
        panel_width,
        40 * mm,
        "Robin speaks quietly from my shoulder.",
    )
    draw_image(
        pdf,
        ROOT / "Adventures/2026-01-25/2026-01-25_robin-bows-to-titania_wide.png",
        MAIN_LEFT + 48.5 * mm,
        image_y,
        panel_width,
        40 * mm,
        "Robin acknowledges Titania.",
    )
    draw_image(
        pdf,
        ROOT / "Adventures/2026-02-21/2026-02-21_find-familiar_finishes_robin-offended_whisper_close.png",
        MAIN_LEFT + 97 * mm,
        image_y,
        panel_width,
        40 * mm,
        "The familiar objection, correctly delivered.",
    )
    cursor = image_y - 9 * mm
    left_top = cursor
    right_top = cursor
    left_top = draw_box(
        pdf,
        MAIN_LEFT,
        left_top,
        68 * mm,
        "Personality",
        [
            "Quiet, observant, loyal by choice, and capable of immediate offence when reduced to a category beneath her.",
            "She comments on beauty others miss, including the lovely noise of a Shadowfell aspen. Her glow contracts or expands with the grace of a place.",
        ],
        style=BODY_SMALL,
    )
    right_top = draw_box(
        pdf,
        MAIN_LEFT + 74 * mm,
        right_top,
        MAIN_RIGHT - (MAIN_LEFT + 74 * mm),
        "Fae knowledge",
        [
            "Robin recognises layered versions of places. At the Circle of Dreams she said the Material and Fae versions correspond, though the Fae version is grander.",
            "She described the Faerealm as cyclic: abandonment is not necessarily an ending; people may return.",
        ],
        style=BODY_SMALL,
    )
    cursor = min(left_top, right_top) - 6 * mm
    observations = [
        ["OBSERVATION", "RECORDED RESULT"],
        ["Void realm", "Followed Voltaire; retreated with him when hordes approached."],
        ["Shadowfell aspen", "Heard beauty; glow became more contained during meditation."],
        ["Titania", "Bowed to the statue and spoke with layered-plane familiarity."],
        ["Tower", "Appeared after Voltaire's six-month statue vigil, apparently summoned."],
        ["Divine plan", "Chose to remain with Voltaire for the intended journey toward Arvandor."],
    ]
    cursor = draw_table(pdf, observations, MAIN_LEFT, cursor, [43 * mm, 98 * mm], font_size=6.8)
    cursor -= 6 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "History in one sentence",
        [
            "Born from improbable sunlight, tested by void, educated by layered worlds, and still present when a new god finally began taking attendance.",
        ],
        style=QUOTE,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 10 * mm, "She notices grace the way I notice mechanisms.", SHADOW_PURPLE, 2),
            (TOP - 81 * mm, "A quieter glow may mean the darkness is behaving politely.", MUTED_GREEN, -3),
            (TOP - 154 * mm, "Cyclic does not mean safe. It means the map breathes.", DRIED_BLOOD, 3),
            (TOP - 220 * mm, "Loyalty is divine only when it can leave.", SHADOW_PURPLE, -2),
        ],
    )
    pdf.showPage()

    # Leaf III - the deliberately incomplete mechanics.
    draw_parchment(pdf, 203, 3, "Machinations & Actions: 5e - Robin, First Disciple")
    cursor = draw_running_header(pdf, "Companion Article III", "Mechanical Lacunae, Preserved Honestly")
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "No invented stat block",
        [
            "Robin's mechanics have not been confirmed by Lachlan. The catalogue therefore records each unknown as unknown. A blank is not an invitation to make a person less true.",
        ],
        style=BODY_SMALL,
        fill=colors.HexColor("#d9c9a1"),
    )
    cursor -= 6 * mm
    registry = [
        ["FIELD", "STATUS"],
        ["Maximum HP / Hit Die / HP per level", "UNRESOLVED"],
        ["Armour Class and adjustments", "UNRESOLVED"],
        ["Initiative / movement / climb / swim / fly", "UNRESOLVED"],
        ["Proficiency bonus / passive perception", "UNRESOLVED"],
        ["Vision / other senses", "UNRESOLVED"],
        ["STR / DEX / CON / INT / WIS / CHA", "UNRESOLVED"],
        ["Saving throws", "UNRESOLVED"],
        ["Resistances / immunities", "UNRESOLVED"],
        ["Skills / tools / weapon or armour training", "UNRESOLVED"],
        ["Languages", "Speaks with Voltaire; mechanical languages UNRESOLVED"],
        ["Carrying / push-drag-lift / weight carried", "UNRESOLVED"],
        ["Feats / additional features", "UNRESOLVED"],
        ["Equipment", "None confirmed as personally carried"],
    ]
    cursor = draw_table(pdf, registry, MAIN_LEFT, cursor, [78 * mm, 63 * mm], font_size=6.6)
    cursor -= 6 * mm
    known = [
        ["KNOWN NARRATIVE CAPABILITY", "BOUNDARY"],
        ["Independent speech and judgement", "Confirmed"],
        ["Flight or hovering by luminous wings", "Visually observed; exact speed unknown"],
        ["Variable glow", "Observed; radius and mechanics unknown"],
        ["Planar or Fae-layer knowledge", "Observed; scope unknown"],
        ["Apparent summoning or sudden appearance", "Observed once; mechanism unknown"],
        ["Blessing of V", "Granted; every mechanical effect unknown"],
    ]
    cursor = draw_table(pdf, known, MAIN_LEFT, cursor, [70 * mm, 71 * mm], font_size=6.7)
    cursor -= 6 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Proposed questions for Lachlan",
        [
            "What creature type is Robin? Does she have a complete companion stat block? Can she be summoned, dismissed, targeted as a familiar, or resurrected? What changed when she received the Blessing of V?",
        ],
        style=BODY_SMALL,
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 11 * mm, "Unknown is a measurement, not a failure.", SHADOW_PURPLE, -2),
            (TOP - 78 * mm, "No autopsy will be conducted for administrative convenience.", DRIED_BLOOD, 3),
            (TOP - 150 * mm, "Flight speed: visibly sufficient.", MUTED_GREEN, -3),
            (TOP - 219 * mm, "If Find Familiar fails, perhaps the spell should apologise.", DRIED_BLOOD, 2),
        ],
    )
    pdf.showPage()

    # Leaf IV - blessing and covenant.
    draw_parchment(pdf, 204, 4, "Machinations & Actions: 5e - Robin, First Disciple")
    cursor = draw_running_header(pdf, "Companion Article IV", "Blessing, Covenant, and Intended Future")
    draw_image(
        pdf,
        ROOT / "Adventures/2026-07-25/2026-07-25_robin-blessing-of-v.png",
        MAIN_LEFT,
        cursor - 71 * mm,
        76 * mm,
        71 * mm,
        "The Blessing of V is bestowed; its workings remain unmeasured.",
    )
    cursor_right = draw_box(
        pdf,
        MAIN_LEFT + 82 * mm,
        cursor,
        MAIN_RIGHT - (MAIN_LEFT + 82 * mm),
        "The words",
        [
            '"As a token of appreciation for your divine loyalty, I give you the Blessing of V."',
            "The blessing is narratively confirmed. Appearance, bond, abilities, resources, limits, and cost remain unresolved.",
        ],
        style=BODY_SMALL,
    )
    cursor_right -= 6 * mm
    cursor_right = draw_box(
        pdf,
        MAIN_LEFT + 82 * mm,
        cursor_right,
        MAIN_RIGHT - (MAIN_LEFT + 82 * mm),
        "The covenant",
        [
            "Robin pledged to be my guiding light in the dark - my sun.",
            "I pledged to be her moonlight.",
        ],
        style=QUOTE,
    )
    cursor = min(cursor - 78 * mm, cursor_right) - 6 * mm
    cursor = draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Role in the proposed divinity",
        [
            "Robin is the clearest proof that a follower need not be erased to belong. She retains judgement, disagreement, and the right to call a ritual foolish.",
            "Her intended place is not beneath the new god but beside the threshold: light that can enter darkness without pretending darkness has ceased to exist.",
        ],
        style=BODY_SMALL,
    )
    cursor -= 6 * mm
    future = [
        ["INTENDED FUTURE", "STATUS"],
        ["Accompany Voltaire toward Arvandor", "Declared"],
        ["Witness or advise the First Rite", "Possible; not yet resolved"],
        ["Clarify the Blessing of V", "Ask Lachlan"],
        ["Discover her own nature and limits", "Open"],
        ["Remain the sun to Voltaire's moonlight", "Mutually pledged"],
    ]
    cursor = draw_table(pdf, future, MAIN_LEFT, cursor, [68 * mm, 73 * mm], font_size=6.9)
    cursor -= 6 * mm
    draw_box(
        pdf,
        MAIN_LEFT,
        cursor,
        MAIN_RIGHT - MAIN_LEFT,
        "Closing classification",
        [
            "<b>Robin:</b> disciple, companion, witness, independent light, probable theological complication, and friend.",
        ],
        style=QUOTE,
        fill=colors.HexColor("#dec187"),
    )
    draw_marginalia(
        pdf,
        [
            (TOP - 9 * mm, "A blessing is not a leash.", DRIED_BLOOD, -3),
            (TOP - 76 * mm, "Sun and moon: different lights, shared sky.", SHADOW_PURPLE, 2),
            (TOP - 151 * mm, "Do not resolve her mystery by reducing her.", MUTED_GREEN, -2),
            (TOP - 220 * mm, "First disciple. First witness. First objection.", DRIED_BLOOD, 3),
        ],
    )
    pdf.showPage()
    pdf.save()
    return output_path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    register_fonts()

    voltaire_path = voltaire_pdf()
    robin_path = robin_pdf()
    print(voltaire_path)
    print(robin_path)


if __name__ == "__main__":
    main()
