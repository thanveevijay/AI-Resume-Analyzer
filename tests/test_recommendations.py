import unittest
from resume_analyzer.recommendations import build_recommendations


class RecommendationTests(unittest.TestCase):
    def test_missing_skills_generate_suggestions(self):
        result = build_recommendations({"missing": ["aws"]})
        self.assertIn("aws", result[0])

    def test_no_missing_skills_returns_review_reminder(self):
        result = build_recommendations({"missing": []})
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
