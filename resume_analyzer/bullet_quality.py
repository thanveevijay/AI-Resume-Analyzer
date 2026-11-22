"""Lightweight checks for clarity of resume project and experience bullets."""
from __future__ import annotations

import re

ACTION_VERBS = {
    "built", "created", "designed", "developed", "implemented", "improved",
    "automated", "analyzed", "deployed", "optimized", "reduced", "increased",
}


def inspect_bullet(text: str) -> dict[str, object]:
    content = text.strip().lstrip("-•* ").strip()
    words = re.findall(r"\b\w+\b", content)
    starts_with_action = bool(words) and words[0].lower() in ACTION_VERBS
    has_number = bool(re.search(r"\b\d+(?:\.\d+)?%?\b", content))
    return {
        "word_count": len(words),
        "starts_with_action_verb": starts_with_action,
        "contains_quantified_detail": has_number,
        "suggestion": (
            "Add a truthful measurable result if available."
            if not has_number else "Review whether the quantified result has clear context."
        ),
    }
