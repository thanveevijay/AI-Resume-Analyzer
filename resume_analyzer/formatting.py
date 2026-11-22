"""Normalize resume bullet text for consistent display."""
from __future__ import annotations

import re


def clean_bullet(text: str) -> str:
    value = text.strip()
    value = re.sub(r"^[\s•*\-]+", "", value)
    value = re.sub(r"\s+", " ", value)
    return value


def clean_lines(text: str) -> list[str]:
    return [clean_bullet(line) for line in text.splitlines() if clean_bullet(line)]
