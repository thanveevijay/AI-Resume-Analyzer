import unittest
from resume_analyzer.report_html import render_html


class HtmlReportTests(unittest.TestCase):
    def test_renders_report_content_safely(self):
        report = {
            "comparison": {"matched": ["python"], "missing": ["sql<script>"]},
            "score": {"score": 50, "interpretation": "heuristic"},
            "recommendations": ["Add evidence for SQL"],
            "disclaimer": "Not a hiring decision",
        }
        html = render_html(report)
        self.assertIn("python", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<script>", html)


if __name__ == "__main__":
    unittest.main()
