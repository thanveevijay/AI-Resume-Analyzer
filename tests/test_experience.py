import unittest
from resume_analyzer.experience import stated_experience_years


class ExperienceTests(unittest.TestCase):
    def test_detects_explicit_year_mentions(self):
        self.assertEqual(stated_experience_years("3 years in Python and 2+ yrs in SQL"), [3, 2])

    def test_does_not_infer_dates(self):
        self.assertEqual(stated_experience_years("Worked from 2020 to 2024"), [])


if __name__ == "__main__":
    unittest.main()
