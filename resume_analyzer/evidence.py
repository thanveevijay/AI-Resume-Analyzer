"""Find short text snippets that support detected skill mentions."""
from __future__ import annotations

from .text_utils import normalize_text


def evidence_for_skills(text: str, skills: list[str], max_chars: int = 180) -> dict[str, list[str]]:
    if max_chars < 20:
        raise ValueError("max_chars must be at least 20")
    sentences = [part.strip() for part in text.replace("\n", ". ").split(".") if part.strip()]
    result: dict[str, list[str]] = {}
    for skill in skills:
        matches = [
            sentence[:max_chars]
            for sentence in sentences
            if skill.lower() in normalize_text(sentence)
        ]
        result[skill] = matches[:3]
    return result
