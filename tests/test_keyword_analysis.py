import unittest
from resume_analyzer.keyword_analysis import important_terms


class KeywordAnalysisTests(unittest.TestCase):
    def test_returns_frequent_terms(self):
        terms = important_terms("Python Python SQL SQL SQL teamwork", limit=2)
        self.assertEqual(terms[0], ("sql", 3))

    def test_limit_must_be_positive(self):
        with self.assertRaises(ValueError):
            important_terms("Python", 0)


if __name__ == "__main__":
    unittest.main()
