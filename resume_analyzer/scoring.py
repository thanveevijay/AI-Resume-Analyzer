"""Explainable heuristic scoring; not a hiring prediction model."""
from __future__ import annotations


def skill_match_score(matched: list[str], required: list[str]) -> float:
    required_set = set(required)
    if not required_set:
        return 0.0
    return round(100.0 * len(set(matched) & required_set) / len(required_set), 2)


def score_breakdown(comparison: dict[str, list[str]]) -> dict[str, float | int | str]:
    required = comparison.get("job_skills", [])
    matched = comparison.get("matched", [])
    score = skill_match_score(matched, required)
    return {
        "score": score,
        "matched_count": len(set(matched) & set(required)),
        "required_count": len(set(required)),
        "method": "matched required skills / detected required skills",
        "interpretation": "heuristic skill coverage; not a probability of interview or employment",
    }
