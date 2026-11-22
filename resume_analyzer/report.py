"""Structured report assembly and JSON serialization."""
from __future__ import annotations

import json
from datetime import datetime, timezone


def build_report(comparison: dict, score: dict, recommendations: list[str]) -> dict:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "comparison": comparison,
        "score": score,
        "recommendations": recommendations,
        "disclaimer": "Heuristic analysis only. Review context and do not use as an automated hiring decision.",
    }


def to_json(report: dict, indent: int = 2) -> str:
    return json.dumps(report, indent=indent, ensure_ascii=False)
