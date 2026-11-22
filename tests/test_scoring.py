import unittest
from resume_analyzer.scoring import skill_match_score, score_breakdown


class ScoringTests(unittest.TestCase):
    def test_full_match(self):
        self.assertEqual(skill_match_score(["python", "sql"], ["python", "sql"]), 100.0)

    def test_partial_match(self):
        self.assertEqual(skill_match_score(["python"], ["python", "sql"]), 50.0)

    def test_empty_requirements(self):
        self.assertEqual(skill_match_score([], []), 0.0)

    def test_score_breakdown_disclaimer(self):
        result = score_breakdown({"matched": ["python"], "job_skills": ["python", "sql"]})
        self.assertIn("not a probability", result["interpretation"])


if __name__ == "__main__":
    unittest.main()
