"""Text normalization utilities used by the analysis pipeline."""
from __future__ import annotations

import re
import unicodedata


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = unicodedata.normalize("NFKC", text).lower()
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    normalized = normalize_text(text)
    return re.findall(r"[a-z0-9]+(?:[+#.]|-[a-z0-9]+)?", normalized)
