import unittest
from resume_analyzer.education import extract_education_lines


class EducationTests(unittest.TestCase):
    def test_extracts_degree_lines(self):
        lines = extract_education_lines("Education\nB.Tech Computer Science\nPython projects")
        self.assertEqual(lines, ["B.Tech Computer Science"])

    def test_empty_when_no_degree_terms(self):
        self.assertEqual(extract_education_lines("Coursework in Python"), [])


if __name__ == "__main__":
    unittest.main()
