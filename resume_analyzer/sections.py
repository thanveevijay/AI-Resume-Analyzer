"""Identify common resume sections without assuming a fixed layout."""
from __future__ import annotations

import re

HEADINGS = {
    "summary": ("summary", "profile", "objective", "professional summary"),
    "experience": ("experience", "work experience", "employment history"),
    "education": ("education", "academic background"),
    "projects": ("projects", "personal projects", "academic projects"),
    "skills": ("skills", "technical skills", "core competencies"),
    "certifications": ("certifications", "certificates", "licenses"),
}


def split_sections(text: str) -> dict[str, str]:
    lines = text.splitlines()
    result: dict[str, list[str]] = {}
    current = "unclassified"
    result[current] = []
    lookup = {heading: key for key, values in HEADINGS.items() for heading in values}
    for line in lines:
        candidate = re.sub(r"[:\s]+$", "", line.strip().lower())
        if candidate in lookup:
            current = lookup[candidate]
            result.setdefault(current, [])
        else:
            result.setdefault(current, []).append(line)
    return {key: "\n".join(value).strip() for key, value in result.items() if "\n".join(value).strip()}
