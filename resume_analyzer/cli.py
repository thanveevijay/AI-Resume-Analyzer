"""Command-line entry point for resume analysis."""
from __future__ import annotations

import argparse
from pathlib import Path

from .extractor import extract_text
from .matcher import compare_skills
from .scoring import score_breakdown
from .recommendations import build_recommendations
from .report import build_report, to_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resume", required=True, help="Path to resume file")
    parser.add_argument("--job-description", required=True, help="Path to job description text file")
    parser.add_argument("--output", help="Optional JSON report output path")
    args = parser.parse_args()

    resume_text = extract_text(args.resume)
    job_text = Path(args.job_description).read_text(encoding="utf-8")
    comparison = compare_skills(resume_text, job_text)
    report = build_report(comparison, score_breakdown(comparison), build_recommendations(comparison))
    rendered = to_json(report)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
