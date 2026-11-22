import unittest
from resume_analyzer.phrase_match import contains_phrase


class PhraseMatchTests(unittest.TestCase):
    def test_matches_full_skill_phrase(self):
        self.assertTrue(contains_phrase("Experience with machine learning models", "machine learning"))

    def test_avoids_substring_false_positive(self):
        self.assertFalse(contains_phrase("Used SQLAlchemy", "sql"))

    def test_case_insensitive(self):
        self.assertTrue(contains_phrase("PYTHON developer", "python"))


if __name__ == "__main__":
    unittest.main()
