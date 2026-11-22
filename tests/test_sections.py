import unittest
from resume_analyzer.sections import split_sections


class SectionTests(unittest.TestCase):
    def test_splits_known_sections(self):
        result = split_sections("Summary\nPython developer\nSkills:\nPython, SQL")
        self.assertEqual(result["summary"], "Python developer")
        self.assertEqual(result["skills"], "Python, SQL")

    def test_preserves_unclassified_content(self):
        result = split_sections("Alex Morgan\nComputer Science")
        self.assertIn("unclassified", result)


if __name__ == "__main__":
    unittest.main()
