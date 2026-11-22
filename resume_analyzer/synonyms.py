"""Optional, transparent skill synonym expansion."""
from __future__ import annotations

DEFAULT_SYNONYMS = {
    "postgres": "postgresql",
    "js": "javascript",
    "ml": "machine learning",
    "dl": "deep learning",
    "powerbi": "power bi",
}


def canonicalize_skill(skill: str, synonyms: dict[str, str] | None = None) -> str:
    mapping = synonyms or DEFAULT_SYNONYMS
    value = skill.strip().lower()
    return mapping.get(value, value)
