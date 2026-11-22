"""Extract frequent job-description terms not already covered by skills."""
from __future__ import annotations

from collections import Counter
from .text_utils import tokenize

STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "our", "are", "will",
    "have", "has", "this", "that", "from", "into", "their", "they",
    "job", "role", "work", "team", "years", "year", "ability",
}


def important_terms(text: str, limit: int = 20) -> list[tuple[str, int]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    counts = Counter(
        token for token in tokenize(text)
        if len(token) > 2 and token not in STOPWORDS
    )
    return counts.most_common(limit)
