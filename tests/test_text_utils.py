import unittest
from resume_analyzer.text_utils import normalize_text, tokenize


class TextUtilsTests(unittest.TestCase):
    def test_normalizes_case_and_whitespace(self):
        self.assertEqual(normalize_text("  PYTHON   SQL "), "python sql")

    def test_tokenizes_text(self):
        self.assertIn("python", tokenize("Python, SQL and C++"))

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            normalize_text(None)


if __name__ == "__main__":
    unittest.main()
