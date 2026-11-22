import unittest
from resume_analyzer.pipeline import analyze_text


class PipelineTests(unittest.TestCase):
    def test_pipeline_returns_explainable_report(self):
        report = analyze_text(
            "Built Python APIs and used SQL for reporting in projects.",
            "Required Python, SQL and AWS skills for the role.",
        )
        self.assertEqual(report["score"]["score"], 66.67)
        self.assertIn("aws", report["comparison"]["missing"])
        self.assertIn("python", report["comparison"]["evidence"])


if __name__ == "__main__":
    unittest.main()
