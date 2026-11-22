"""Compare detected skill coverage by taxonomy category."""
from __future__ import annotations

from .skills import flatten_skills


def category_coverage(comparison: dict, taxonomy: dict[str, list[str]] | None = None) -> dict[str, dict[str, int | float]]:
    skill_categories = flatten_skills(taxonomy)
    required = set(comparison.get("job_skills", []))
    matched = set(comparison.get("matched", []))
    result = {}
    for category in sorted(set(skill_categories.values())):
        category_required = {skill for skill in required if skill_categories.get(skill) == category}
        if not category_required:
            continue
        category_matched = category_required & matched
        result[category] = {
            "matched": len(category_matched),
            "required": len(category_required),
            "coverage_percent": round(100 * len(category_matched) / len(category_required), 2),
        }
    return result
