"""File text extraction with optional PDF and DOCX dependencies."""
from __future__ import annotations

from pathlib import Path


class UnsupportedFileError(ValueError):
    pass


def extract_text(path: str | Path) -> str:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(file_path)
    suffix = file_path.suffix.lower()

    if suffix == ".txt":
        return file_path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("Install pypdf to read PDF files.") from exc
        reader = PdfReader(str(file_path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if suffix == ".docx":
        try:
            from docx import Document
        except ImportError as exc:
            raise RuntimeError("Install python-docx to read DOCX files.") from exc
        document = Document(str(file_path))
        return "\n".join(paragraph.text for paragraph in document.paragraphs)
    raise UnsupportedFileError(f"Unsupported file type: {suffix}")
