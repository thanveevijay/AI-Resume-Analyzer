import unittest
from resume_analyzer.synonyms import canonicalize_skill


class SynonymTests(unittest.TestCase):
    def test_default_synonym(self):
        self.assertEqual(canonicalize_skill("ML"), "machine learning")

    def test_custom_synonym(self):
        self.assertEqual(canonicalize_skill("db", {"db": "database"}), "database")


if __name__ == "__main__":
    unittest.main()
