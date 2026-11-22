import unittest
from resume_analyzer.validation import validate_inputs


class ValidationTests(unittest.TestCase):
    def test_accepts_sufficient_text(self):
        validate_inputs("A" * 30, "B" * 30)

    def test_rejects_empty_resume(self):
        with self.assertRaises(ValueError):
            validate_inputs("", "B" * 30)

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            validate_inputs(None, "B" * 30)


if __name__ == "__main__":
    unittest.main()
