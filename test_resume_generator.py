import tempfile
import unittest
from pathlib import Path

import resume_generator as rg


def render(data):
    return rg.generate_html(data, rg.STYLE_CONFIG)


def minimal(**overrides):
    data = {
        "lang": "en",
        "file_name": "Test_CV",
        "name": "Test Person",
        "title": "Backend Engineer",
        "contact": {"email": "test@example.com", "github": "https://github.com/test"},
        "summary": "Summary text.",
        "experience": [],
        "skills": ["Python"],
    }
    data.update(overrides)
    return data


class VariantsTest(unittest.TestCase):
    def test_one_english_resume(self):
        self.assertEqual(rg.list_variants(), ["en"])

    def test_headlines_expand_into_one_resume_each(self):
        data = rg.load_variant("en")
        resumes = rg.expand_headlines(data)
        self.assertEqual(len(resumes), len(data["headlines"]))
        self.assertEqual({r["title"] for r in resumes}, set(data["headlines"].values()))
        for resume in resumes:
            self.assertEqual(resume["summary"], data["summary"])

    def test_without_headlines_the_resume_is_unchanged(self):
        data = minimal()
        self.assertEqual(rg.expand_headlines(data), [data])

    def test_variants_carry_no_years_or_commit_share(self):
        for name in rg.list_variants():
            summary = rg.load_variant(name)["summary"]
            for marker in ("2.5+", "2,5+", "35%"):
                self.assertNotIn(marker, summary, name)

    def test_inbulk_leads_with_the_waybill_metric(self):
        for name in rg.list_variants():
            achievements = rg.load_variant(name)["experience"][0]["achievements"]
            self.assertLessEqual(len(achievements), 6, name)
            self.assertIn("0.2" if name.startswith("en") else "0,2", achievements[0], name)

    def test_every_resume_renders_name_and_title(self):
        for name in rg.list_variants():
            for data in rg.expand_headlines(rg.load_variant(name)):
                html = render(data)
                self.assertIn(data["name"], html)
                self.assertIn(data["title"], html)

    def test_resume_file_names_are_unique(self):
        files = [d["file_name"] for n in rg.list_variants() for d in rg.expand_headlines(rg.load_variant(n))]
        self.assertEqual(len(files), len(set(files)))

    def test_build_writes_one_html_per_headline(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = rg.build(rg.list_variants(), out_dir=Path(tmp))
            self.assertEqual(len(built), len(rg.load_variant("en")["headlines"]))
            self.assertTrue(all(p.exists() and p.suffix == ".html" for p in built))


class RenderTest(unittest.TestCase):
    def test_ukrainian_variant_uses_ukrainian_labels(self):
        job = {"position": "P", "company": "C", "location": "L", "period": "2025", "achievements": ["a"]}
        html = render(minimal(lang="uk", experience=[job]))
        self.assertIn('lang="uk"', html)
        self.assertIn("Досвід роботи", html)
        self.assertNotIn(">Experience<", html)

    def test_grouped_skills_show_group_names(self):
        html = render(minimal(skills={"Backend": ["FastAPI"], "Data": ["PostgreSQL"]}))
        for text in ("Backend", "FastAPI", "Data", "PostgreSQL"):
            self.assertIn(text, html)

    def test_flat_skills_still_render(self):
        html = render(minimal(skills=["FastAPI", "Docker"]))
        self.assertIn("FastAPI", html)
        self.assertIn("Docker", html)

    def test_only_black_and_white_colors(self):
        import re
        html = render(minimal())
        colors = {c.lower() for c in re.findall(r"#[0-9a-fA-F]{3,8}\b", html)}
        self.assertLessEqual(colors, {"#000", "#000000", "#fff", "#ffffff"})
        self.assertNotIn("rgb", html)

    def test_section_titles_have_no_letter_spacing(self):
        self.assertNotIn("letter-spacing", render(minimal()))

    def test_single_column_has_no_grid_columns(self):
        html = render(minimal(skills={"Backend": ["FastAPI"]}, education=[{"degree": "D", "school": "S", "period": "2020"}]))
        self.assertNotIn('class="columns"', html)
        self.assertNotIn("grid-template-columns", html)

    def test_certifications_render_issuer_and_link(self):
        cert = {"name": "Course", "issuer": "Issuer", "date": "2026", "id": "ID 1", "link": "https://x.y/c.pdf"}
        html = render(minimal(certifications=[cert, "Plain line"]))
        self.assertIn("Issuer, 2026, ID 1", html)
        self.assertIn('<a href="https://x.y/c.pdf">x.y/c.pdf</a>', html)
        self.assertIn("Plain line", html)

    def test_projects_render_every_link(self):
        proj = {"name": "P", "description": "d", "links": [{"text": "A", "url": "https://a"}, {"url": "https://b.c/d"}]}
        html = render(minimal(projects=[proj]))
        self.assertIn('A: <a href="https://a">a</a>', html)
        self.assertIn('href="https://b.c/d">b.c/d<', html)

    def test_projects_render_bullets(self):
        proj = {"name": "P", "bullets": ["first point", "second point"]}
        html = render(minimal(projects=[proj]))
        self.assertIn("<li>first point</li><li>second point</li>", html)

    def test_contacts_show_readable_links(self):
        html = render(minimal())
        self.assertIn(">github.com/test<", html)
        self.assertIn('href="mailto:test@example.com"', html)

    def test_talks_render_with_link(self):
        talk = {"title": "Talk", "event": "Meetup", "date": "08/2026", "link": "https://youtu.be/x"}
        html = render(minimal(talks=[talk, "Plain community line"]))
        self.assertIn('<a href="https://youtu.be/x">youtu.be/x</a>', html)
        self.assertIn("Plain community line", html)


if __name__ == "__main__":
    unittest.main()
