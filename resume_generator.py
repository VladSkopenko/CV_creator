#!/usr/bin/env python3
"""
Resume Generator: renders single-column, ATS-friendly A4 resumes to HTML and, optionally, to PDF
through headless Chrome.

Every resume variant is a file in variants/ that defines RESUME_DATA.

    python resume_generator.py          # build all variants into output/
    python resume_generator.py en       # build one variant and open it in the browser
    python resume_generator.py --pdf    # also export PDFs (needs Google Chrome)
"""

import argparse
import importlib
import shutil
import subprocess
import tempfile
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VARIANTS_DIR = ROOT / "variants"
OUTPUT_DIR = ROOT / "output"

STYLE_CONFIG = {
    "accent_color": "#1a5276",
    "text_color": "#1f2933",
    "light_text": "#5f6b7a",
    "rule_color": "#dde3ea",
    "background": "#ffffff",
    "font_family": "Arial, 'Helvetica Neue', Helvetica, sans-serif",
}

LABELS = {
    "en": {
        "summary": "Summary",
        "skills": "Skills",
        "experience": "Experience",
        "projects": "Projects",
        "education": "Education",
        "certifications": "Certifications",
        "languages": "Languages",
        "talks": "Talks & media",
    },
    "uk": {
        "summary": "Профіль",
        "skills": "Навички",
        "experience": "Досвід роботи",
        "projects": "Проєкти",
        "education": "Освіта",
        "certifications": "Сертифікати",
        "languages": "Мови",
        "talks": "Виступи та медіа",
    },
}

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "chrome",
)


def _readable_url(url: str) -> str:
    return url.split("://", 1)[-1].removeprefix("www.").rstrip("/")


def _section(title: str, body: str) -> str:
    return f'<section class="section"><h2>{title}</h2>{body}</section>'


def _links(items: list) -> str:
    return " · ".join(f'<a href="{item["url"]}">{item.get("text") or _readable_url(item["url"])}</a>' for item in items)


def render_contacts(contact: dict) -> str:
    parts = []
    if contact.get("location"):
        parts.append(f"<span>{contact['location']}</span>")
    if contact.get("phone"):
        parts.append(f'<a href="tel:{contact["phone"].replace(" ", "")}">{contact["phone"]}</a>')
    if contact.get("email"):
        parts.append(f'<a href="mailto:{contact["email"]}">{contact["email"]}</a>')
    for key in ("linkedin", "github", "website", "telegram"):
        if contact.get(key):
            parts.append(f'<a href="{contact[key]}">{_readable_url(contact[key])}</a>')
    return ' <span class="sep">·</span> '.join(parts)


def _skill_items(items: list) -> str:
    return ", ".join(f'<span class="nowrap">{item}</span>' for item in items)


def render_skills(skills, label: str) -> str:
    if not skills:
        return ""
    if isinstance(skills, dict):
        rows = "".join(
            f'<p class="skill-row"><strong>{group}:</strong> {_skill_items(items)}</p>' for group, items in skills.items()
        )
        return _section(label, rows)
    return _section(label, f'<p class="skill-row">{_skill_items(skills)}</p>')


def render_experience(items: list, extra: list, label: str) -> str:
    blocks = []
    for exp in items:
        company = exp["company"]
        if exp.get("company_url"):
            company = f'<a href="{exp["company_url"]}">{company}</a>'
        location = f'<span class="loc"> · {exp["location"]}</span>' if exp.get("location") else ""
        description = f'<p class="exp-desc">{exp["description"]}</p>' if exp.get("description") else ""
        bullets = "".join(f"<li>{achievement}</li>" for achievement in exp.get("achievements", []))
        blocks.append(
            '<div class="exp">'
            f'<div class="row"><span class="position">{exp["position"]}</span>'
            f'<span class="period">{exp["period"]}</span></div>'
            f'<div class="company">{company}{location}</div>'
            f"{description}"
            f'<ul class="bullets">{bullets}</ul>'
            "</div>"
        )
    if extra:
        blocks.append('<ul class="extra">' + "".join(f"<li>{line}</li>" for line in extra) + "</ul>")
    return _section(label, "".join(blocks)) if blocks else ""


def render_projects(items: list, label: str) -> str:
    if not items:
        return ""
    blocks = []
    for proj in items:
        links = list(proj.get("links", []))
        if proj.get("link"):
            links.insert(0, {"url": proj["link"]})
        meta = " · ".join(part for part in (proj.get("period"), proj.get("stack")) if part)
        head = f'<div class="row"><span class="project-name">{proj["name"]}</span><span class="period">{meta}</span></div>'
        links_html = f'<p class="project-links">{_links(links)}</p>' if links else ""
        blocks.append(f'<div class="project">{head}<p>{proj["description"]}</p>{links_html}</div>')
    return _section(label, "".join(blocks))


def render_education(items: list, label: str) -> str:
    if not items:
        return ""
    blocks = []
    for edu in items:
        details = f'<p class="edu-details">{edu["details"]}</p>' if edu.get("details") else ""
        blocks.append(
            f'<div class="edu"><div class="row"><span class="degree">{edu["degree"]}</span>'
            f'<span class="period">{edu["period"]}</span></div>'
            f'<div class="school">{edu["school"]}</div>{details}</div>'
        )
    return _section(label, "".join(blocks))


def render_certifications(items: list, label: str) -> str:
    if not items:
        return ""
    lines = []
    for item in items:
        if isinstance(item, str):
            lines.append(f"<li>{item}</li>")
            continue
        meta = ", ".join(part for part in (item.get("issuer"), item.get("date"), item.get("id")) if part)
        link = f' · <a href="{item["link"]}">{item.get("link_text", "link")}</a>' if item.get("link") else ""
        lines.append(f'<li><strong>{item["name"]}</strong> — {meta}{link}</li>')
    return _section(label, f'<ul class="plain">{"".join(lines)}</ul>')


def render_languages(items: list, label: str) -> str:
    if not items:
        return ""
    text = " · ".join(f'<strong>{lang["language"]}</strong>: {lang["level"]}' for lang in items)
    return _section(label, f'<p class="languages">{text}</p>')


def render_talks(talks: list, label: str) -> str:
    if not talks:
        return ""
    blocks = []
    for talk in talks:
        if isinstance(talk, str):
            blocks.append(f'<p class="talk-note">{talk}</p>')
            continue
        meta = " · ".join(part for part in (talk.get("event"), talk.get("date")) if part)
        if talk.get("link"):
            meta += f' · <a href="{talk["link"]}">{talk.get("link_text", "link")}</a>'
        description = f'<p class="talk-desc">{talk["description"]}</p>' if talk.get("description") else ""
        blocks.append(
            f'<div class="talk"><div class="row"><span class="talk-title">{talk["title"]}</span>'
            f'<span class="period">{meta}</span></div>{description}</div>'
        )
    return _section(label, "".join(blocks))


def build_css(s: dict) -> str:
    return f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
@page {{ size: A4; margin: 10mm 12mm 10mm 12mm; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{
    font-family: {s['font_family']};
    font-size: 9.2pt;
    line-height: 1.3;
    color: {s['text_color']};
    background: #e9edf1;
}}
a {{ color: {s['accent_color']}; text-decoration: none; }}
.resume {{
    width: 210mm;
    min-height: 297mm;
    margin: 24px auto;
    padding: 10mm 12mm 10mm 12mm;
    background: {s['background']};
    box-shadow: 0 2px 24px rgba(15, 23, 42, 0.12);
}}
.header {{ padding-bottom: 2.4mm; margin-bottom: 2.8mm; border-bottom: 1.5px solid {s['accent_color']}; }}
.name {{ font-size: 20pt; font-weight: 700; line-height: 1.1; }}
.title {{ font-size: 11pt; font-weight: 700; color: {s['accent_color']}; margin-top: 1.2mm; }}
.contacts {{ font-size: 8.6pt; color: {s['light_text']}; margin-top: 1.8mm; line-height: 1.55; }}
.contacts a, .contacts span {{ white-space: nowrap; }}
.sep {{ color: #b7c1cc; margin: 0 0.5mm; }}
.section {{ margin-bottom: 2.6mm; }}
.section h2 {{
    font-size: 9pt;
    font-weight: 700;
    color: {s['accent_color']};
    text-transform: uppercase;
    letter-spacing: 0.12em;
    padding-bottom: 0.8mm;
    margin-bottom: 1.5mm;
    border-bottom: 1px solid {s['rule_color']};
}}
.summary {{ font-size: 9.2pt; }}
.skill-row {{ margin-bottom: 0.6mm; }}
.nowrap {{ white-space: nowrap; }}
.exp, .project, .edu, .talk {{ margin-bottom: 2mm; break-inside: avoid; }}
.row {{ display: flex; justify-content: space-between; align-items: baseline; gap: 4mm; }}
.position, .project-name, .degree, .talk-title {{ font-size: 10pt; font-weight: 700; }}
.period {{ font-size: 8.6pt; color: {s['light_text']}; white-space: nowrap; }}
.company {{ font-size: 9.2pt; font-weight: 700; color: {s['accent_color']}; margin-top: 0.2mm; }}
.company .loc {{ font-weight: 400; color: {s['light_text']}; }}
.exp-desc {{ font-size: 9pt; color: {s['light_text']}; margin-top: 0.4mm; }}
.bullets {{ margin: 1.1mm 0 0 4mm; }}
.bullets li {{ margin-bottom: 0.5mm; padding-left: 0.5mm; }}
.bullets li::marker {{ color: {s['accent_color']}; }}
.extra {{ list-style: none; margin-top: 1.2mm; }}
.extra li {{ margin-bottom: 0.6mm; }}
.project p {{ margin-top: 0.4mm; }}
.project-links {{ font-size: 8.8pt; }}
.school {{ font-size: 9pt; color: {s['accent_color']}; }}
.edu-details {{ font-size: 8.8pt; color: {s['light_text']}; }}
.plain {{ margin-left: 4mm; }}
.plain li {{ margin-bottom: 0.6mm; }}
.talk-desc, .talk-note {{ margin-top: 0.3mm; }}
@media print {{
    body {{ background: #ffffff; }}
    .resume {{ width: auto; min-height: 0; margin: 0; padding: 0; box-shadow: none; }}
}}
"""


def generate_html(data: dict, style: dict) -> str:
    lang = data.get("lang", "en")
    labels = LABELS.get(lang, LABELS["en"])

    summary = data.get("summary", "").strip()
    summary_html = _section(labels["summary"], f'<p class="summary">{summary}</p>') if summary else ""
    body = (
        summary_html
        + render_skills(data.get("skills"), labels["skills"])
        + render_experience(data.get("experience", []), data.get("extra_experience", []), labels["experience"])
        + render_projects(data.get("projects", []), labels["projects"])
        + render_education(data.get("education", []), labels["education"])
        + render_certifications(data.get("certifications", []), labels["certifications"])
        + render_languages(data.get("languages", []), labels["languages"])
        + render_talks(data.get("talks", []), labels["talks"])
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{data['name']} · {data['title']}</title>
<style>{build_css(style)}</style>
</head>
<body>
<div class="resume">
<header class="header">
<h1 class="name">{data['name']}</h1>
<div class="title">{data['title']}</div>
<div class="contacts">{render_contacts(data.get('contact', {}))}</div>
</header>
{body}
</div>
</body>
</html>
"""


def list_variants() -> list[str]:
    return sorted(path.stem for path in VARIANTS_DIR.glob("*.py") if not path.stem.startswith("_"))


def load_variant(name: str) -> dict:
    return importlib.import_module(f"variants.{name}").RESUME_DATA


def find_chrome() -> str | None:
    for candidate in CHROME_CANDIDATES:
        found = candidate if Path(candidate).is_absolute() and Path(candidate).exists() else shutil.which(candidate)
        if found:
            return found
    return None


def export_pdf(html_path: Path, pdf_path: Path, chrome: str) -> None:
    with tempfile.TemporaryDirectory() as profile_dir:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--user-data-dir={profile_dir}",
                f"--print-to-pdf={pdf_path}",
                html_path.resolve().as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )


def build(names: list[str], out_dir: Path = OUTPUT_DIR, pdf: bool = False) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    chrome = find_chrome() if pdf else None
    if pdf and chrome is None:
        print("Google Chrome not found: PDFs skipped. Open the HTML in a browser and print it to PDF.")
    built = []
    for name in names:
        data = load_variant(name)
        html_path = out_dir / f"{data['file_name']}.html"
        html_path.write_text(generate_html(data, STYLE_CONFIG), encoding="utf-8")
        built.append(html_path)
        if chrome:
            pdf_path = html_path.with_suffix(".pdf")
            export_pdf(html_path, pdf_path, chrome)
            built.append(pdf_path)
    return built


def main(argv: list[str] | None = None) -> None:
    available = list_variants()
    parser = argparse.ArgumentParser(description="Render resume variants to HTML and, optionally, PDF.")
    parser.add_argument("variants", nargs="*", help=f"variants to build, default all: {', '.join(available)}")
    parser.add_argument("--pdf", action="store_true", help="also export PDFs with headless Google Chrome")
    args = parser.parse_args(argv)

    unknown = sorted(set(args.variants) - set(available))
    if unknown:
        parser.error(f"unknown variant(s): {', '.join(unknown)}")
    names = args.variants or available

    built = build(names, pdf=args.pdf)
    for path in built:
        print(f"  {path.relative_to(ROOT)}")
    if len(names) == 1:
        webbrowser.open(built[0].resolve().as_uri())


if __name__ == "__main__":
    main()
