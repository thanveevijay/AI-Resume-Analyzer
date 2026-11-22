"""Skill extraction and transparent job requirement matching."""
from __future__ import annotations

from .skills import flatten_skills
from .text_utils import normalize_text


def find_skills(text: str, taxonomy: dict[str, list[str]] | None = None) -> list[str]:
    normalized = normalize_text(text)
    found = []
    for skill in flatten_skills(taxonomy):
        if skill in normalized:
            found.append(skill)
    return sorted(set(found))


def compare_skills(resume_text: str, job_text: str) -> dict[str, list[str]]:
    resume_skills = set(find_skills(resume_text))
    job_skills = set(find_skills(job_text))
    return {
        "matched": sorted(resume_skills & job_skills),
        "missing": sorted(job_skills - resume_skills),
        "additional": sorted(resume_skills - job_skills),
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
    }
