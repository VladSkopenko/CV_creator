#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resume Generator - Generate beautiful HTML/PDF resumes
Run this script to generate a professional resume in HTML format
"""

import webbrowser
from pathlib import Path

# ============================================
# FILL IN YOUR DATA HERE ↓↓↓
# ============================================

RESUME_DATA = {
    "name": "Vladyslav Skopenko",
    "title": "Python Developer",
    
    "contact": {
        "location": "Odesa, Ukraine",
        "phone": "+380 63 193 40 48",
        "email": "skopirka2k17@gmail.com",
        "linkedin": "https://www.linkedin.com/in/vladyslav-skopenko/",
        "github": "https://github.com/VladSkopenko",
        "website": "https://vladskopenko.github.io/",
    },
    
    "summary": """
        Python Backend Developer with 2+ years of experience building scalable web applications. 
        Proven track record as a top contributor (84% of codebase) on B2B platforms serving 2,000+ companies and 10,000+ users. 
        Experienced in both small agile teams (3 people) and large cross-functional teams (20+ members). 
        Strong expertise in FastAPI, async SQLAlchemy, PostgreSQL, and cloud deployments.
    """,
    
    "experience": [
        {
            "position": "Python Developer",
            "company": "iCORN",
            "location": "Kyiv, Ukraine (Remote)",
            "period": "03/2025 - Present",
            "achievements": [
                "Top contributor (84% of codebase) on B2B commodity trading platform serving 2,000+ companies and 10,000+ users",
                "Engineered universal OAuth 2.0 authentication (Google, LinkedIn, Meta), replacing Auth0 and saving $24K annually",
                "Built Dashboard analytics with 2,100+ lines of optimized SQL/CTE queries for complex aggregations and multi-currency calculations",
                "Developed Logistics module: transport management, waybill documents, driver tracking with Google Maps integration",
                "Implemented Auction system with orders, bidding, counter-offers, and templates functionality",
                "Created Document automation: PDF generation with digital signature verification, Excel parsing for bulk imports",
                "Designed 187 database migrations (80% ownership) with async SQLAlchemy 2.0 and query optimization",
                "Performance optimization on datasets with millions of records, N+1 query elimination, load testing",
                "Built real-time notifications (WebSocket), Telegram bot for logistics automation",
                "Integrations: Odoo ERP, S3 storage (boto3), Google Maps API, DigitalOcean deployment",
                "DevOps: Docker deployment, Prometheus monitoring, 5 background workers, CI/CD (GitHub/GitLab)",
            ]
        },
        {
            "position": "Python Mentor",
            "company": "GoIT",
            "location": "Kyiv, Ukraine (Remote)",
            "period": "11/2024 - 01/2025",
            "achievements": [
                "Mentored students in Python programming, fostering a positive learning environment and encouraging technical growth",
                "Conducted thorough code reviews providing constructive feedback and ensuring high-quality code standards",
                "Offered technical consultations to clarify complex concepts and guide students through project challenges",
            ]
        },
        {
            "position": "Python Developer",
            "company": "Aurveda",
            "location": "Ukraine (Remote, Contract)",
            "period": "05/2024 - 08/2024",
            "achievements": [
                "Built full-featured Telegram e-commerce bot using Aiogram, completely replacing traditional online store",
                "Implemented scheduled auto-posting system to multiple Telegram channels for marketing automation",
                "Developed admin panel for staff to manage and update products inventory in real-time",
                "Created customer support chat system using Telegram API for seamless user communication",
                "Integrated KeyCRM for order management, customer data sync, and business analytics",
                "Deployed on DigitalOcean with Docker, ensuring high availability and scalability",
            ]
        },
        {
            "position": "Software Developer",
            "company": "Tekra",
            "location": "Remote (Part-time)",
            "period": "03/2024 - Present",
            "achievements": [
                "Developed desktop application using Python and PyQt library with efficient user interface",
                "Optimized multithreading, improving application performance and reducing data processing time",
                "Built automation bots for various tasks streamlining business processes",
                "Participated in frontend website development, ensuring fast and responsive user experience",
                "Built backend services using FastAPI, providing high-performance and scalable APIs",
            ]
        },
    ],
    
    "education": [
        {
            "degree": "Bachelor's degree, Finance and Banking",
            "school": "Odesa National Economic University",
            "period": "2017 - 2021",
            "details": "",
        },
    ],
    
    "skills": [
        "Python 3.12",
        "FastAPI",
        "SQLAlchemy 2.0",
        "PostgreSQL",
        "Alembic",
        "Pydantic v2",
        "Docker",
        "Docker Compose",
        "WebSocket",
        "Git",
        "GitLab",
        "GitHub",
        "Aiogram",
        "Postman",
        "REST API",
        "OAuth 2.0",
        "DigitalOcean",
        "S3 / boto3",
        "Google Maps API",
        "Prometheus",
        "CI/CD",
        "PyQt",
        "Multithreading",
        "Mentoring",
    ],
    
    "languages": [
        {"language": "Ukrainian", "level": "Native"},
        {"language": "English", "level": "B1-B2 (Intermediate)"},
    ],
    
    "certifications": [
        "Python Developer — GoIT Academy, 2023 - 2024",
    ],
    
    "projects": [],
}

# ============================================
# STYLE SETTINGS
# ============================================

STYLE_CONFIG = {
    "accent_color": "#1a5276",      # Accent color (sidebar and headings)
    "text_color": "#2c3e50",        # Main text color
    "light_text": "#666666",        # Secondary text color
    "background": "#ffffff",        # Background color
    "sidebar_width": "6px",         # Sidebar width
    "font_family": "'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif",
}

# ============================================
# HTML GENERATION (don't touch unless you know what you're doing)
# ============================================

def generate_html(data: dict, style: dict) -> str:
    """Generates HTML code for resume"""
    
    # Contact information
    contact_parts = []
    c = data["contact"]
    if c.get("location"):
        contact_parts.append(c["location"])
    if c.get("phone"):
        contact_parts.append(c["phone"])
    if c.get("email"):
        contact_parts.append(f'<a href="mailto:{c["email"]}">{c["email"]}</a>')
    if c.get("linkedin"):
        contact_parts.append(f'<a href="{c["linkedin"]}" target="_blank">LinkedIn</a>')
    if c.get("github"):
        contact_parts.append(f'<a href="{c["github"]}" target="_blank">GitHub</a>')
    if c.get("website"):
        contact_parts.append(f'<a href="{c["website"]}" target="_blank">Portfolio</a>')
    
    contact_html = ' &nbsp;•&nbsp; '.join(contact_parts)
    
    # Summary
    summary_html = f"""
    <section class="section">
        <h2>Summary</h2>
        <p class="summary-text">{data['summary'].strip()}</p>
    </section>
    """ if data.get("summary") and data["summary"].strip() else ""
    
    # Experience
    experience_html = ""
    if data.get("experience"):
        exp_items = ""
        for exp in data["experience"]:
            achievements = "\n".join([f"<li>{a}</li>" for a in exp.get("achievements", [])])
            exp_items += f"""
            <div class="experience-item">
                <div class="exp-header">
                    <div class="exp-title">
                        <span class="position">{exp['position']}</span>
                        <span class="period">{exp['period']}</span>
                    </div>
                    <div class="exp-company">{exp['company']}, {exp['location']}</div>
                </div>
                <ul class="achievements">
                    {achievements}
                </ul>
            </div>
            """
        experience_html = f"""
        <section class="section">
            <h2>Experience</h2>
            {exp_items}
        </section>
        """
    
    # Education
    education_html = ""
    if data.get("education"):
        edu_items = ""
        for edu in data["education"]:
            details = f'<p class="edu-details">{edu["details"]}</p>' if edu.get("details") else ""
            edu_items += f"""
            <div class="education-item">
                <div class="edu-header">
                    <span class="degree">{edu['degree']}</span>
                    <span class="period">{edu['period']}</span>
                </div>
                <div class="school">{edu['school']}</div>
                {details}
            </div>
            """
        education_html = f"""
        <section class="section">
            <h2>Education</h2>
            {edu_items}
        </section>
        """
    
    # Skills
    skills_html = ""
    if data.get("skills"):
        skills_list = "".join([f"<li>{skill}</li>" for skill in data["skills"]])
        skills_html = f"""
        <section class="section">
            <h2>Skills</h2>
            <ul class="skills-list">
                {skills_list}
            </ul>
        </section>
        """
    
    # Languages
    languages_html = ""
    if data.get("languages"):
        lang_items = "".join([f"<li><strong>{l['language']}</strong> — {l['level']}</li>" for l in data["languages"]])
        languages_html = f"""
        <section class="section">
            <h2>Languages</h2>
            <ul class="languages-list">
                {lang_items}
            </ul>
        </section>
        """
    
    # Certifications
    certs_html = ""
    if data.get("certifications"):
        cert_items = "".join([f"<li>{cert}</li>" for cert in data["certifications"]])
        certs_html = f"""
        <section class="section">
            <h2>Certifications</h2>
            <ul class="cert-list">
                {cert_items}
            </ul>
        </section>
        """
    
    # Projects
    projects_html = ""
    if data.get("projects"):
        proj_items = ""
        for proj in data["projects"]:
            link = f' — <a href="{proj["link"]}" target="_blank">View Project</a>' if proj.get("link") else ""
            proj_items += f"""
            <div class="project-item">
                <strong>{proj['name']}</strong>{link}
                <p>{proj['description']}</p>
            </div>
            """
        projects_html = f"""
        <section class="section">
            <h2>Projects</h2>
            {proj_items}
        </section>
        """
    
    # Full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['name']} - Resume</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        @page {{
            size: A4;
            margin: 0;
        }}
        
        body {{
            font-family: {style['font_family']};
            font-size: 11pt;
            line-height: 1.5;
            color: {style['text_color']};
            background: #f0f0f0;
        }}
        
        .resume {{
            max-width: 210mm;
            min-height: 297mm;
            margin: 20px auto;
            background: {style['background']};
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            display: flex;
        }}
        
        .sidebar {{
            width: {style['sidebar_width']};
            background: {style['accent_color']};
            flex-shrink: 0;
        }}
        
        .content {{
            flex: 1;
            padding: 40px 45px;
        }}
        
        /* Header */
        .header {{
            text-align: center;
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .name {{
            font-size: 28pt;
            font-weight: 600;
            color: {style['text_color']};
            margin-bottom: 5px;
            letter-spacing: 1px;
        }}
        
        .title {{
            font-size: 13pt;
            color: {style['accent_color']};
            font-weight: 500;
            margin-bottom: 15px;
        }}
        
        .contact {{
            font-size: 9.5pt;
            color: {style['light_text']};
        }}
        
        .contact a {{
            color: {style['accent_color']};
            text-decoration: none;
        }}
        
        .contact a:hover {{
            text-decoration: underline;
        }}
        
        /* Sections */
        .section {{
            margin-bottom: 22px;
        }}
        
        .section h2 {{
            font-size: 12pt;
            font-weight: 600;
            color: {style['accent_color']};
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 2px solid {style['accent_color']};
        }}
        
        /* Summary */
        .summary-text {{
            text-align: justify;
            color: {style['text_color']};
        }}
        
        /* Experience */
        .experience-item {{
            margin-bottom: 18px;
        }}
        
        .experience-item:last-child {{
            margin-bottom: 0;
        }}
        
        .exp-header {{
            margin-bottom: 8px;
        }}
        
        .exp-title {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}
        
        .position {{
            font-weight: 600;
            font-size: 11pt;
            color: {style['text_color']};
        }}
        
        .period {{
            font-size: 10pt;
            color: {style['light_text']};
        }}
        
        .exp-company {{
            font-size: 10pt;
            color: {style['accent_color']};
            font-weight: 500;
        }}
        
        .achievements {{
            margin-left: 18px;
            margin-top: 6px;
        }}
        
        .achievements li {{
            margin-bottom: 4px;
            text-align: justify;
        }}
        
        /* Education */
        .education-item {{
            margin-bottom: 12px;
        }}
        
        .edu-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }}
        
        .degree {{
            font-weight: 600;
            font-size: 11pt;
        }}
        
        .school {{
            color: {style['accent_color']};
            font-size: 10pt;
        }}
        
        .edu-details {{
            font-size: 10pt;
            color: {style['light_text']};
            margin-top: 4px;
        }}
        
        /* Skills */
        .skills-list {{
            display: flex;
            flex-wrap: wrap;
            list-style: none;
            gap: 8px 15px;
        }}
        
        .skills-list li {{
            position: relative;
            padding-left: 12px;
        }}
        
        .skills-list li::before {{
            content: "•";
            position: absolute;
            left: 0;
            color: {style['accent_color']};
            font-weight: bold;
        }}
        
        /* Languages */
        .languages-list {{
            list-style: none;
        }}
        
        .languages-list li {{
            margin-bottom: 4px;
        }}
        
        /* Certifications */
        .cert-list {{
            margin-left: 18px;
        }}
        
        .cert-list li {{
            margin-bottom: 4px;
        }}
        
        /* Projects */
        .project-item {{
            margin-bottom: 10px;
        }}
        
        .project-item p {{
            font-size: 10pt;
            margin-top: 3px;
        }}
        
        .project-item a {{
            color: {style['accent_color']};
            text-decoration: none;
        }}
        
        /* Print styles */
        @media print {{
            body {{
                background: white;
            }}
            
            .resume {{
                box-shadow: none;
                margin: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="resume">
        <div class="sidebar"></div>
        <div class="content">
            <header class="header">
                <h1 class="name">{data['name']}</h1>
                <div class="title">{data['title']}</div>
                <div class="contact">{contact_html}</div>
            </header>
            
            {summary_html}
            {experience_html}
            {education_html}
            {skills_html}
            {languages_html}
            {certs_html}
            {projects_html}
        </div>
    </div>
</body>
</html>"""
    
    return html


def main():
    """Main function - generates resume and opens in browser"""
    
    # Generate HTML
    html_content = generate_html(RESUME_DATA, STYLE_CONFIG)
    
    # Save file
    output_path = Path(__file__).parent / "resume.html"
    output_path.write_text(html_content, encoding="utf-8")
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    ✅ RESUME GENERATED!                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📄 File: {str(output_path):<50} ║
║                                                              ║
║  📝 How to use:                                              ║
║     1. Open this script and fill in your data               ║
║        in RESUME_DATA variable                               ║
║     2. Run the script: python resume_generator.py            ║
║     3. Resume will open in your browser                      ║
║     4. Press Ctrl+P (or Cmd+P on Mac) → Save as PDF         ║
║                                                              ║
║  🎨 Want to change colors? Edit STYLE_CONFIG                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # Открываем в браузере
    webbrowser.open(f"file://{output_path.absolute()}")


if __name__ == "__main__":
    main()

