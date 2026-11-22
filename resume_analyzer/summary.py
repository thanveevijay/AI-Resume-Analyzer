"""Generate a concise, evidence-based analysis summary."""
from __future__ import annotations


def analysis_summary(comparison: dict, score: dict) -> str:
    matched = len(comparison.get("matched", []))
    missing = len(comparison.get("missing", []))
    total = len(comparison.get("job_skills", []))
    value = score.get("score", 0)
    return (
        f"Detected {matched} of {total} job-description skills "
        f"({value}% heuristic coverage); {missing} detected requirements "
        "were not found in the resume text."
    )
