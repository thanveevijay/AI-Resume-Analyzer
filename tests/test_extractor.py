import tempfile
import unittest
from pathlib import Path
from resume_analyzer.extractor import extract_text, UnsupportedFileError


class ExtractorTests(unittest.TestCase):
    def test_reads_utf8_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "resume.txt"
            path.write_text("Python developer", encoding="utf-8")
            self.assertEqual(extract_text(path), "Python developer")

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            extract_text("does-not-exist.txt")

    def test_unsupported_file_raises(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "resume.xyz"
            path.write_text("sample", encoding="utf-8")
            with self.assertRaises(UnsupportedFileError):
                extract_text(path)


if __name__ == "__main__":
    unittest.main()
