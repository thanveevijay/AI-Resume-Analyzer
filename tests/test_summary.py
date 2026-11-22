import unittest
from resume_analyzer.summary import analysis_summary


class SummaryTests(unittest.TestCase):
    def test_summary_counts_skill_coverage(self):
        text = analysis_summary(
            {"matched": ["python"], "missing": ["sql"], "job_skills": ["python", "sql"]},
            {"score": 50.0},
        )
        self.assertIn("1 of 2", text)
        self.assertIn("50.0%", text)


if __name__ == "__main__":
    unittest.main()
