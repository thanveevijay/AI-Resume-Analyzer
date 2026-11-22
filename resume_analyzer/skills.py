"""Transparent, editable skill taxonomy for resume analysis."""
from __future__ import annotations

DEFAULT_SKILLS = {
    "programming": ["python", "java", "c", "c++", "javascript", "typescript"],
    "data": ["sql", "pandas", "numpy", "power bi", "tableau", "excel"],
    "machine_learning": ["machine learning", "deep learning", "scikit-learn", "pytorch", "tensorflow"],
    "cloud": ["aws", "azure", "google cloud", "docker", "kubernetes"],
    "web": ["html", "css", "react", "node.js", "flask", "django", "fastapi"],
    "engineering": ["git", "github", "linux", "rest api", "testing", "ci/cd"],
}


def flatten_skills(taxonomy: dict[str, list[str]] | None = None) -> dict[str, str]:
    taxonomy = taxonomy or DEFAULT_SKILLS
    result: dict[str, str] = {}
    for category, skills in taxonomy.items():
        for skill in skills:
            result[skill.lower()] = category
    return result
