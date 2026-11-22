import unittest
from resume_analyzer.role_fit import category_coverage


class RoleFitTests(unittest.TestCase):
    def test_category_coverage(self):
        result = category_coverage(
            {"job_skills": ["python", "sql", "aws"], "matched": ["python", "aws"]}
        )
        self.assertEqual(result["programming"]["coverage_percent"], 100.0)
        self.assertEqual(result["data"]["coverage_percent"], 0.0)


if __name__ == "__main__":
    unittest.main()
