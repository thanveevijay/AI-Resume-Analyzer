"""Render a self-contained HTML report from an analysis result."""
from __future__ import annotations

from html import escape


def render_html(report: dict) -> str:
    comparison = report.get("comparison", {})
    score = report.get("score", {})
    matched = "".join(f"<li>{escape(str(x))}</li>" for x in comparison.get("matched", []))
    missing = "".join(f"<li>{escape(str(x))}</li>" for x in comparison.get("missing", []))
    suggestions = "".join(f"<li>{escape(str(x))}</li>" for x in report.get("recommendations", []))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Resume Analysis</title>
<style>body{{font:16px system-ui;max-width:850px;margin:40px auto;padding:0 20px;line-height:1.5}}section{{border:1px solid #ddd;border-radius:10px;padding:16px;margin:16px 0}}.score{{font-size:2rem;font-weight:700}}</style>
</head><body><h1>Resume Analysis</h1>
<p class="score">{escape(str(score.get("score", 0)))} / 100</p>
<p>{escape(str(score.get("interpretation", "Heuristic analysis")))}</p>
<section><h2>Matched skills</h2><ul>{matched or "<li>None detected</li>"}</ul></section>
<section><h2>Missing skills</h2><ul>{missing or "<li>None detected</li>"}</ul></section>
<section><h2>Suggestions</h2><ul>{suggestions}</ul></section>
<p><small>{escape(str(report.get("disclaimer", "")))}</small></p></body></html>"""
