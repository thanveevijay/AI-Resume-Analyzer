"""High-level orchestration for the resume analysis workflow."""
from __future__ import annotations

from .matcher import compare_skills
from .scoring import score_breakdown
from .recommendations import build_recommendations
from .report import build_report
from .validation import validate_inputs
from .evidence import evidence_for_skills


def analyze_text(resume_text: str, job_text: str) -> dict:
    validate_inputs(resume_text, job_text)
    comparison = compare_skills(resume_text, job_text)
    comparison["evidence"] = evidence_for_skills(resume_text, comparison["matched"])
    return build_report(
        comparison,
        score_breakdown(comparison),
        build_recommendations(comparison),
    )
