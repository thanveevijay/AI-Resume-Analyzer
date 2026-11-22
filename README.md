# AI Resume Analyzer

A modular Python project that extracts resume text, compares it with a job description, and produces an explainable skills and keyword analysis. It is an assistive tool: its score is a heuristic, not a hiring decision.

## Features
- Extract text from TXT, PDF, and DOCX files (PDF/DOCX dependencies are optional).
- Normalize text and identify skills from a transparent skill dictionary.
- Compare resume skills with job requirements.
- Report matched, missing, and additional skills.
- Highlight important job-description terms and provide actionable suggestions.
- Export a structured JSON report.

## Quick start
```bash
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
python -m resume_analyzer.cli --resume samples/sample_resume.txt --job-description samples/sample_job_description.txt
```

## Project structure
- `resume_analyzer/`: extraction, parsing, matching, scoring, recommendations, and reporting.
- `tests/`: unit tests.
- `samples/`: fictional sample inputs.
- `docs/`: design, privacy, evaluation, and usage notes.

## Responsible use
Do not use the heuristic score as an automated hiring decision. Resume data is personal information. Process files locally, obtain consent, avoid retaining uploads unnecessarily, and review recommendations for context and bias.
