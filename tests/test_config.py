import json
import tempfile
import unittest
from pathlib import Path
from resume_analyzer.config import load_taxonomy


class ConfigTests(unittest.TestCase):
    def test_loads_taxonomy(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skills.json"
            path.write_text(json.dumps({"data": ["SQL", "Python"]}), encoding="utf-8")
            self.assertEqual(load_taxonomy(path), {"data": ["sql", "python"]})

    def test_rejects_invalid_taxonomy(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skills.json"
            path.write_text('{"data": "python"}', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_taxonomy(path)


if __name__ == "__main__":
    unittest.main()
