import unittest
from resume_analyzer.report import build_report, to_json


class ReportTests(unittest.TestCase):
    def test_report_is_json_serializable(self):
        report = build_report({"matched": ["python"]}, {"score": 100}, ["Review evidence"])
        rendered = to_json(report)
        self.assertIn('"python"', rendered)
        self.assertIn("not an automated hiring decision", rendered)


if __name__ == "__main__":
    unittest.main()
