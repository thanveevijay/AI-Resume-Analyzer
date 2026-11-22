"""Extract likely education lines from a detected education section."""
from __future__ import annotations

DEGREE_TERMS = (
    "bachelor", "master", "b.tech", "b.e.", "b.sc", "m.sc",
    "ph.d", "diploma", "associate",
)


def extract_education_lines(text: str) -> list[str]:
    lines = [line.strip(" -•\t") for line in text.splitlines() if line.strip()]
    return [
        line for line in lines
        if any(term in line.lower() for term in DEGREE_TERMS)
    ]
