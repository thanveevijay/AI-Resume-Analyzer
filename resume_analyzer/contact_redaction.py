"""Best-effort contact detail masking for logs and previews."""
from __future__ import annotations

import re

EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\w)(?:\+?\d[\d ()-]{7,}\d)(?!\w)")


def redact_contacts(text: str) -> str:
    text = EMAIL.sub("[EMAIL REDACTED]", text)
    return PHONE.sub("[PHONE REDACTED]", text)
