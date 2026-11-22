import unittest
from resume_analyzer.bullet_quality import inspect_bullet


class BulletQualityTests(unittest.TestCase):
    def test_action_verb_and_metric(self):
        result = inspect_bullet("Built a dashboard that reduced report time by 30%")
        self.assertTrue(result["starts_with_action_verb"])
        self.assertTrue(result["contains_quantified_detail"])

    def test_does_not_invent_metrics(self):
        result = inspect_bullet("Worked on a Python project")
        self.assertFalse(result["contains_quantified_detail"])
        self.assertIn("truthful", result["suggestion"])


if __name__ == "__main__":
    unittest.main()
