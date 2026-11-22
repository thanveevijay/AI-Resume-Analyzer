import unittest
from resume_analyzer.formatting import clean_bullet, clean_lines


class FormattingTests(unittest.TestCase):
    def test_removes_bullet_prefix(self):
        self.assertEqual(clean_bullet("  • Built an API "), "Built an API")

    def test_removes_blank_lines(self):
        self.assertEqual(clean_lines("One\n\n- Two"), ["One", "Two"])


if __name__ == "__main__":
    unittest.main()
