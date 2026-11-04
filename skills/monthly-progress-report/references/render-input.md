# Renderer input

Install PyMuPDF in the available Python environment if it is missing. This helper uses no cloud services. Run:

```text
python scripts/render_report.py content.json --output report.pdf --html report.html
```

Paths are resolved from the current directory. Optional `--regular-font` and `--bold-font` select a matching font pair. Otherwise the renderer looks for Arial on Windows, Arial on macOS, or DejaVu Sans on Linux and falls back to PDF Helvetica for supported characters. It fails on unsupported characters or page overflow instead of silently dropping content. Split a long page into another page or edit the prose if it overflows. Do not reduce the body below a readable size to force a page count.

The JSON uses this structure. `status`, page `title`, section `heading`, `paragraphs`, and `bullets` are optional. Heading `level` is 1 by default, or 2 for a smaller project label.

```json
{
  "title": "Monthly progress report | AI Cell",
  "name": "Report author",
  "designation": "AI Engineer",
  "period": "October 2026",
  "status": "Draft for review",
  "pages": [
    {
      "sections": [
        {"heading": "1. Project-wise progress"},
        {"heading": "a. Project name | Delivered in October", "level": 2},
        {"heading": "More reliable file preparation", "paragraphs": ["Describe the verified issue, change and practical benefit in natural prose."]}
      ]
    },
    {
      "title": "Project name | Continued",
      "sections": [
        {"heading": "Next month", "bullets": ["A confirmed priority or clearly proposed draft priority."]},
        {"heading": "4. Overall remarks", "paragraphs": ["-"]}
      ]
    }
  ]
}
```

The renderer checks layout and glyph coverage, not the truth of report content. Keep sources and unresolved questions in a separate private ledger. The HTML is an editable companion; PDF page images remain the visual QA target.
