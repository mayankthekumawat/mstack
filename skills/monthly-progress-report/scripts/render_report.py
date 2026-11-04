"""Render an explicitly paged monthly report to PDF and optional editable HTML."""

import argparse
import html
import json
from pathlib import Path

import fitz


INK = (0.12, 0.15, 0.20)
MUTED = (0.34, 0.38, 0.44)
ACCENT = (0.12, 0.28, 0.45)
WIDTH, HEIGHT = fitz.paper_size("a4")
LEFT, RIGHT, BOTTOM = 51, WIDTH - 51, HEIGHT - 55


def font_pair(regular, bold):
    if bool(regular) != bool(bold):
        raise ValueError("Supply both --regular-font and --bold-font")
    pairs = [(regular, bold)] if regular else [
        ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
        ("/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    for r, b in pairs:
        if Path(r).is_file() and Path(b).is_file():
            return {"R": fitz.Font(fontfile=r), "B": fitz.Font(fontfile=b)}
    if regular:
        raise ValueError("Both supplied font files must exist")
    return {"R": fitz.Font("helv"), "B": fitz.Font("hebo")}


class Writer:
    def __init__(self, page, fonts):
        self.page, self.fonts, self.y = page, fonts, 55
        for key, font in fonts.items():
            page.insert_font(fontname=key, fontbuffer=font.buffer)

    def text(self, value, size=10.2, font="R", color=INK, indent=0, leading=13.6, after=4):
        if not isinstance(value, str):
            raise ValueError("Report text must be a string")
        face = self.fonts[font]
        missing = {c for c in value if not c.isspace() and not face.has_glyph(ord(c))}
        if missing:
            raise ValueError(f"Unsupported font characters: {sorted(missing)}; choose another font pair")
        lines = []
        for paragraph in value.splitlines() or [""]:
            current = ""
            for word in paragraph.split():
                if face.text_length(word, fontsize=size) > RIGHT - LEFT - indent:
                    raise ValueError(f"Unbreakable word exceeds page width: {word[:60]}")
                candidate = f"{current} {word}".strip()
                if current and face.text_length(candidate, fontsize=size) > RIGHT - LEFT - indent:
                    lines.append(current)
                    current = word
                else:
                    current = candidate
            lines.append(current)
        if self.y + leading * len(lines) + after > BOTTOM:
            raise ValueError(f"Page {self.page.number + 1} overflows near {value[:70]!r}; split the page")
        for line in lines:
            self.page.insert_text((LEFT + indent, self.y), line, fontname=font, fontsize=size, color=color)
            self.y += leading
        self.y += after

    def heading(self, value, level=1):
        self.y += 5 if level == 1 else 2
        self.text(value, size=11.3 if level == 1 else 10.3, font="B",
                  color=ACCENT if level == 1 else INK, after=3)

    def bullet(self, value):
        y = self.y
        self.text(value, indent=12, after=3)
        self.page.draw_circle((LEFT + 2, y - 3.2), 1.4, color=INK, fill=INK)


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Report content must be a JSON object")
    for key in ("title", "name", "designation", "period"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} must be nonempty text")
    if not isinstance(data.get("status", ""), str):
        raise ValueError("status must be text")
    if not isinstance(data.get("pages"), list) or not data["pages"]:
        raise ValueError("pages must be a nonempty array")
    for page in data["pages"]:
        if not isinstance(page, dict) or not isinstance(page.get("sections"), list) or not page["sections"]:
            raise ValueError("Each page needs a nonempty sections array")
        if not isinstance(page.get("title", ""), str):
            raise ValueError("Page title must be text")
        for section in page["sections"]:
            if not isinstance(section, dict) or not isinstance(section.get("heading", ""), str):
                raise ValueError("Each section must be an object with an optional text heading")
            if section.get("level", 1) not in (1, 2):
                raise ValueError("Heading level must be 1 or 2")
            for key in ("paragraphs", "bullets"):
                values = section.get(key, [])
                if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                    raise ValueError(f"{key} must be an array of text strings")


def render(data, pdf_path, html_path=None, regular=None, bold=None):
    validate(data)
    fonts = font_pair(regular, bold)
    doc = fitz.open()
    esc = html.escape
    html_pages = []
    for index, page_data in enumerate(data["pages"]):
        page = doc.new_page(width=WIDTH, height=HEIGHT)
        writer = Writer(page, fonts)
        parts = []
        if index == 0:
            writer.text(data["title"], size=20, font="B", leading=25, after=7)
            identity = f"Name: {data['name']} | Designation: {data['designation']}"
            writer.text(identity, size=10.3, after=1)
            writer.text(f"Month: {data['period']}", size=10.3, after=9)
            parts.extend([f"<h1>{esc(data['title'])}</h1>", f"<p>{esc(identity)}<br>Month: {esc(data['period'])}</p>"])
            if data.get("status"):
                writer.text(data["status"], size=9, color=MUTED, after=7)
                parts.append(f"<p class='status'>{esc(data['status'])}</p>")
        elif page_data.get("title"):
            writer.text(page_data["title"], size=16, font="B", leading=22, after=5)
            parts.append(f"<h1 class='continued'>{esc(page_data['title'])}</h1>")
        for section in page_data["sections"]:
            if section.get("heading"):
                level = section.get("level", 1)
                writer.heading(section["heading"], level)
                tag = "h2" if level == 1 else "h3"
                parts.append(f"<{tag}>{esc(section['heading'])}</{tag}>")
            for paragraph in section.get("paragraphs", []):
                writer.text(paragraph)
                parts.append(f"<p>{esc(paragraph)}</p>")
            if section.get("bullets"):
                parts.append("<ul>")
                for bullet in section["bullets"]:
                    writer.bullet(bullet)
                    parts.append(f"<li>{esc(bullet)}</li>")
                parts.append("</ul>")
        footer = f"{data['name']} | {data['period']}"
        page.insert_text((LEFT, HEIGHT - 27), footer, fontname="R", fontsize=8, color=MUTED)
        count = f"{index + 1} / {len(data['pages'])}"
        x = RIGHT - fonts["R"].text_length(count, fontsize=8)
        page.insert_text((x, HEIGHT - 27), count, fontname="R", fontsize=8, color=MUTED)
        parts.append(f"<footer><span>{esc(footer)}</span><span>{count}</span></footer>")
        html_pages.append("<section class='page'>" + "\n".join(parts) + "</section>")
    doc.set_metadata({"title": f"{data['title']} | {data['period']}", "author": data["name"], "subject": data.get("status", "Monthly progress report")})
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(pdf_path, garbage=4, deflate=True)
    doc.close()
    if html_path:
        html_path.parent.mkdir(parents=True, exist_ok=True)
        css = """@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;background:#eee;color:#1f2633;font:10.2pt/13.6pt Arial,sans-serif}.page{position:relative;width:210mm;min-height:297mm;margin:20px auto;padding:39pt 51pt 65pt;background:white;page-break-after:always}h1{font-size:20pt;line-height:25pt;margin:0 0 12pt}h1.continued{font-size:16pt}h2{font-size:11.3pt;color:#1f4773;margin:9pt 0 3pt;break-after:avoid}h3{font-size:10.3pt;margin:6pt 0 3pt}p{margin:0 0 4pt}ul{padding-left:12pt;margin:0}li{padding-left:0;margin-bottom:3pt}.status{font-size:9pt;color:#576170}footer{position:absolute;bottom:23pt;left:51pt;right:51pt;display:flex;justify-content:space-between;font-size:8pt;color:#576170}@media print{body{background:white}.page{margin:0}}"""
        html_path.write_text("<!doctype html><html lang='en'><meta charset='utf-8'><title>" + esc(data["title"]) + "</title><style>" + css + "</style><body>" + "\n".join(html_pages) + "</body></html>", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("content", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--html", type=Path)
    parser.add_argument("--regular-font")
    parser.add_argument("--bold-font")
    args = parser.parse_args()
    try:
        data = json.loads(args.content.read_text(encoding="utf-8-sig"))
        render(data, args.output, args.html, args.regular_font, args.bold_font)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Report not rendered: {exc}\n")
    print(f"Rendered {len(data['pages'])} pages: {args.output}")


if __name__ == "__main__":
    main()
