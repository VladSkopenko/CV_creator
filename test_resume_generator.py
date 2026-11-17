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
    def test_both_variants_exist(self):
        self.assertEqual(rg.list_variants(), ["en", "uk"])

    def test_every_variant_renders_name_and_title(self):
        for name in rg.list_variants():
            data = rg.load_variant(name)
            html = render(data)
            self.assertIn(data["name"], html)
            self.assertIn(data["title"], html)

    def test_variant_file_names_are_unique(self):
        files = [rg.load_variant(n)["file_name"] for n in rg.list_variants()]
        self.assertEqual(len(files), len(set(files)))

    def test_build_writes_one_html_per_variant(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = rg.build(rg.list_variants(), out_dir=Path(tmp))
            self.assertEqual(len(built), 2)
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

    def test_single_column_has_no_grid_columns(self):
        html = render(minimal(skills={"Backend": ["FastAPI"]}, education=[{"degree": "D", "school": "S", "period": "2020"}]))
        self.assertNotIn('class="columns"', html)
        self.assertNotIn("grid-template-columns", html)

    def test_certifications_render_issuer_and_link(self):
        cert = {"name": "Course", "issuer": "Issuer", "date": "2026", "id": "ID 1", "link": "https://x.y/c.pdf"}
        html = render(minimal(certifications=[cert, "Plain line"]))
        self.assertIn("Issuer, 2026, ID 1", html)
        self.assertIn('href="https://x.y/c.pdf"', html)
        self.assertIn("Plain line", html)

    def test_projects_render_every_link(self):
        proj = {"name": "P", "description": "d", "links": [{"text": "A", "url": "https://a"}, {"url": "https://b.c/d"}]}
        html = render(minimal(projects=[proj]))
        self.assertIn('href="https://a">A<', html)
        self.assertIn('href="https://b.c/d">b.c/d<', html)

    def test_contacts_show_readable_links(self):
        html = render(minimal())
        self.assertIn(">github.com/test<", html)
        self.assertIn('href="mailto:test@example.com"', html)

    def test_talks_render_with_link(self):
        talk = {"title": "Talk", "event": "Meetup", "date": "08/2026", "link": "https://youtu.be/x"}
        html = render(minimal(talks=[talk, "Plain community line"]))
        self.assertIn('href="https://youtu.be/x"', html)
        self.assertIn("Plain community line", html)


if __name__ == "__main__":
    unittest.main()
