"""Generate practical suggestions from missing skill evidence."""
from __future__ import annotations


def build_recommendations(comparison: dict[str, list[str]]) -> list[str]:
    missing = comparison.get("missing", [])
    if not missing:
        return ["The detected skill list covers all skills found in the job description. Review project evidence and role-specific requirements manually."]
    return [
        f"If you have genuine experience with {skill}, add a concise evidence-based bullet showing how you used it."
        for skill in missing
    ]
