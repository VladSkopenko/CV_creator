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
    "name": "Liudmyla Skopenko",
    "title": "Frontend Developer",

    "contact": {
        "location": "Odesa, Ukraine",
        "phone": "+380 963 61 05 73",
        "email": "luda.skopenko80@gmail.com",
        "linkedin": "https://www.linkedin.com/in/liudmyla-skopenko/",
        "github": "https://github.com/LudSkop",
        "telegram": "https://t.me/Liud_skop"
    },

    "summary": """
Frontend developer who creates modern web applications using Next, React and TypeScript. I have strong knowledge of HTML, CSS and JavaScript, and experience in developing responsive and cross-browser interfaces that are user-friendly and work correctly across different devices. I also have experience deploying projects on Vercel.
I am interested in modern frontend development, improving web application performance and creating clear and user-friendly UX/UI.
I am looking for a Junior Frontend Developer position and want to become part of a team where I can grow, improve my skills, and contribute to the development of the product and the company.
""",

    "skills": [
        "HTML",
        "CSS",
        "JavaScript",
        "TypeScript",
        "React",
        "Next.js",
        "Node.js",
        "React Query",
        "Axios",
        "Git",
        "GitHub",
        "Postman",
        "Figma",
        "Vercel"
       
                    
    ],

    "experience": [
       
         {
            "position": "Frontend Developer",
            "company": "CoffeeJoy",
            "location": "",
            "period": "2025",
            "project_link": "https://ludskop.github.io/CoffeeJoy/",
            "achievements": [ "Developed a team-based web layout project (CoffeeJoy) using HTML and CSS. Collaborated with a team using Git and GitHub workflow. Implemented responsive and structured interface design. Technologies: HTML, CSS, JavaScript, Git, GitHub"
            ]
          
        },
          {
            "position": "Frontend Developer",
            "company": "PawFriends",
            "location": "",
            "period":  "2026",
            "project_link": "https://ludskop.github.io/PawFriends/",
            "achievements": ["Developed a responsive pet care platform (PawFriends) for exploring pets, adoption opportunities, and pet care information. Technologies: HTML, Vite, CSS, JavaScript. Implemented modern responsive UI and adaptive layout."
            ]
        },
        {
            "position": "Frontend Developer",
            "company": "Auth App",
            "location": "",
            "period": "2026",
            "project_link": "https://09-auth-khaki-zeta.vercel.app",
            "achievements": ["Authentication app with login, registration, protected routes and API integration. Technologies: HTML, CSS, JavaScript, TypeScript, React, Next.js, Axios,Vercel, Git, GitHub."
            ]

            
        },
    ],

   "work_experience": [
  {
    "position": "Electronics Assembly Technician",
    "company": "Novotek-Electro",
    "location": "Odesa, Ukraine",
    "period": "2011-2023",
    "achievements": "Performed assembly, mounting, and soldering of electronic components and assemblies of radio-electronic devices. Worked with printed circuit boards and technical documentation, following schematics and engineering drawings. Ensured quality control of assembly processes, tested equipment functionality, and eliminated defects. Complied with production standards and safety regulations."
  }
],


    "education": [
        {
            "degree": "Bachelor's degree, Zootechnics",
            "school": "Myhiia Agricultural College",
            "period": "1995 - 1999",
            "details": ""
        },
         {
            "degree": "Fullstack developer",
            "school": "IT School GolT",
            "period": "2025 - 2026",
            "details": ""
        },
        
        
       
    ],


    "languages": [
        {"language": "English", "level": "Elementary"},
        {"language": "Ukrainian", "level": "Native"}
        
    ],

    "projects": [
       
       
    ]
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
    if c.get("telegram"):
        contact_parts.append(f'<a href="{c["telegram"]}" target="_blank">Telegram</a>')
    
    contact_html = ' &nbsp;•&nbsp; '.join(contact_parts)
    
    # Summary
    summary_html = f"""
    <section class="section">
        <h2>Summary</h2>
        <p class="summary-text">{data['summary'].strip()}</p>
    </section>
    """ if data.get("summary") and data["summary"].strip() else ""

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
    
    
   
  # Experience
    experience_html = ""
    if data.get("experience"):
        exp_items = ""
        for exp in data["experience"]:
            achievements = "\n".join([f"<li>{a}</li>" for a in exp.get("achievements", [])])
            project_link = exp.get("project_link", "")
            
            exp_items += f"""
            <div class="experience-item">
                <div class="exp-header">
                    <div class="exp-title">
                        <span class="position">{exp['position']}</span>
                        <span class="period">{exp['period']}</span>
                    </div>
                    <div class="exp-company">{exp['company']} {exp['location']}</div>
                </div>
                <ul class="achievements">
{achievements}
                </ul>
                {f'<a href="{project_link}" target="_blank" class="project-link">View Project →</a>' if project_link else ''}
            </div>
            """
        experience_html = f"""
        <section class="section">
            <h2>Project Experience</h2>
{exp_items}
        </section>
        """
  
   # Work Experience
    work_experience_html = ""
    if data.get("work_experience"):
        work_items = ""
        for work in data["work_experience"]:
            # Якщо achievements - це строка, розділяємо на речення
            achievements_text = work.get("achievements", "")
            if isinstance(achievements_text, str):
                # Розділяємо строку на речення (точка, крапка-кома)
                sentences = [s.strip() for s in achievements_text.split('.') if s.strip()]
                achievements = "\n".join([f"<li>{s}.</li>" for s in sentences])
            else:
                # Якщо це список
                achievements = "\n".join([f"<li>{a}</li>" for a in achievements_text])
            
            work_items += f"""
            <div class="experience-item">
                <div class="exp-header">
                    <div class="exp-title">
                        <span class="position">{work['position']}</span>
                        <span class="period">{work['period']}</span>
                    </div>
                    <div class="exp-company">{work['company']}, {work['location']}</div>
                </div>
                <ul class="achievements">
{achievements}
                </ul>
            </div>
            """
        work_experience_html = f"""
        <section class="section">
            <h2>Work Experience</h2>
{work_items}
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
            color: {style['accent_color']};
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
         /* Project Link */
        .project-link {{
            display: inline-block;
            margin-top: 10px;
            color: {style['accent_color']};
            text-decoration: none;
            font-weight: 500;
            font-size: 10pt;
        }}
        
        .project-link:hover {{
            text-decoration: underline;
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
            {skills_html}
            {languages_html}
            {experience_html}
            {work_experience_html}
            {education_html}
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

