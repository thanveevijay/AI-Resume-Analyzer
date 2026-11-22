"""Load a custom skill taxonomy from a JSON file."""
from __future__ import annotations

import json
from pathlib import Path


def load_taxonomy(path: str | Path) -> dict[str, list[str]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Taxonomy must be a JSON object.")
    validated: dict[str, list[str]] = {}
    for category, skills in data.items():
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category names must be non-empty strings.")
        if not isinstance(skills, list) or not all(isinstance(x, str) and x.strip() for x in skills):
            raise ValueError(f"Skills for {category!r} must be a list of non-empty strings.")
        validated[category] = [skill.strip().lower() for skill in skills]
    return validated
