# 📄 Resume Generator

A simple Python script that renders single-column, ATS-friendly resumes to HTML and PDF. One data file per language, easy to customize.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📸 Preview

![Resume Preview](image.png)

## ✨ Features

- 🎨 Clean single-column layout that ATS parsers read in order: standard section names, no tables or sidebars
- 📱 A4 paper size, print-ready, flows onto a second page when needed
- 🔗 Clickable links (email, LinkedIn, GitHub, etc.)
- 📝 Multiple sections: Summary, Experience, Education, Skills, Languages, Certifications, Projects
- 🖨️ Easy PDF export via browser print function
- ⚡ No dependencies required (pure Python)

## 🚀 Quick Start

### 1. Clone or download the repository

```bash
git clone https://github.com/VladSkopenko/resume-generator.git
cd resume-generator
```

### 2. Edit your data

Each resume variant is a Python file in `variants/` that defines a `RESUME_DATA` dictionary:
`variants/en.py` and `variants/uk.py`. Shared parts (contacts, jobs, education, certifications) live in
`variants/_common.py`; files starting with `_` are not built. Copy a variant to add a new one.

Supported keys: `lang` (`en` or `uk`, sets section titles), `file_name`, `name`, `title`, `contact`
(`location`, `phone`, `email`, `linkedin`, `github`, `website`, `telegram`), `summary`, `skills`
(a list, or a dict of groups), `experience`, `extra_experience` (one-line entries), `projects`
(`name`, `period`, `stack`, `description`, `links` as `{"text", "url"}`), `education`,
`certifications` (plain strings or `{"name", "issuer", "date", "id", "link", "link_text"}`),
`languages`, `talks` (dicts or plain strings). Sections render in that order, one column.

### 3. Generate your resume

```bash
python resume_generator.py               # build every variant into output/
python resume_generator.py en            # build one variant and open it in the browser
python resume_generator.py --pdf         # also export PDFs with headless Google Chrome
```

### 4. Export to PDF

With `--pdf` the script prints every variant to an A4 PDF next to its HTML. Without Chrome,
open the HTML, press `Cmd+P` (Mac) or `Ctrl+P` (Windows/Linux) and choose **Save as PDF**.

### 5. Run the tests

```bash
python -m unittest test_resume_generator
```

## 🎨 Customization

### Change Colors

Edit the `STYLE_CONFIG` dictionary to customize the appearance:

```python
STYLE_CONFIG = {
    "accent_color": "#1a5276",      # Headings and links
    "text_color": "#1f2933",        # Main text color
    "light_text": "#5f6b7a",        # Secondary text color
    "rule_color": "#dde3ea",        # Section dividers
    "background": "#ffffff",        # Page background
    "font_family": "Arial, 'Helvetica Neue', Helvetica, sans-serif",
}
```

### Popular Color Schemes

**Classic Blue (default)**
```python
"accent_color": "#1a5276"
```

**Modern Teal**
```python
"accent_color": "#008080"
```

**Professional Green**
```python
"accent_color": "#2e7d32"
```

**Elegant Purple**
```python
"accent_color": "#5e35b1"
```

**Bold Red**
```python
"accent_color": "#c62828"
```

## 📁 Project Structure

```
resume-generator/
├── resume_generator.py        # Template, rendering and CLI
├── test_resume_generator.py   # Tests (python -m unittest)
├── variants/
│   ├── _common.py             # Shared data: contacts, jobs, education, certifications
│   ├── en.py                  # English resume
│   └── uk.py                  # Ukrainian resume
├── output/                    # Generated HTML and PDF files
└── README.md
```

## 🤝 Contributing

Feel free to fork this project and customize it for your needs!

## 📝 License

MIT License - feel free to use this for your own resume!

---

Made with ❤️ by [Vladyslav Skopenko](https://github.com/VladSkopenko)

