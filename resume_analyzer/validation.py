"""Input validation helpers for the analysis pipeline."""
from __future__ import annotations


def validate_inputs(resume_text: str, job_text: str, min_chars: int = 20) -> None:
    if not isinstance(resume_text, str) or not isinstance(job_text, str):
        raise TypeError("Resume and job description must be strings.")
    if min_chars < 1:
        raise ValueError("min_chars must be positive.")
    if len(resume_text.strip()) < min_chars:
        raise ValueError("Resume text is too short to analyze.")
    if len(job_text.strip()) < min_chars:
        raise ValueError("Job description is too short to analyze.")
