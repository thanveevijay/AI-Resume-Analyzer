import unittest
from resume_analyzer.matcher import find_skills, compare_skills


class MatcherTests(unittest.TestCase):
    def test_detects_known_skills(self):
        self.assertEqual(find_skills("Built APIs using Python and Flask"), ["flask", "python"])

    def test_compares_resume_and_job_skills(self):
        result = compare_skills("Python SQL", "Python SQL AWS")
        self.assertEqual(result["matched"], ["python", "sql"])
        self.assertEqual(result["missing"], ["aws"])

    def test_ignores_unknown_terms(self):
        self.assertEqual(find_skills("communication teamwork"), [])


if __name__ == "__main__":
    unittest.main()
