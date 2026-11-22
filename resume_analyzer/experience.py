"""Extract conservative year-count mentions from resume text."""
from __future__ import annotations

import re

PATTERN = re.compile(r"\b(\d{1,2})\s*\+?\s*(?:years?|yrs?)\b", re.I)


def stated_experience_years(text: str) -> list[int]:
    """Return explicitly stated year counts; does not infer employment duration."""
    return [int(match.group(1)) for match in PATTERN.finditer(text)]
