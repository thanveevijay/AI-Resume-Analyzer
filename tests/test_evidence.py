import unittest
from resume_analyzer.evidence import evidence_for_skills


class EvidenceTests(unittest.TestCase):
    def test_finds_skill_evidence(self):
        result = evidence_for_skills("Built APIs using Python. Analyzed data.", ["python", "sql"])
        self.assertEqual(len(result["python"]), 1)
        self.assertEqual(result["sql"], [])

    def test_rejects_too_small_limit(self):
        with self.assertRaises(ValueError):
            evidence_for_skills("Python", ["python"], 5)


if __name__ == "__main__":
    unittest.main()
