# Feature Guide

## Extraction
TXT is read directly. PDF and DOCX extraction use optional dependencies listed in `requirements.txt`.

## Matching
The taxonomy is intentionally transparent. Detected skills are matched as phrases, then divided into matched, missing, and additional groups.

## Evidence
Evidence snippets show the resume sentence where a detected skill appears. A keyword mention is not proof of proficiency; human review remains necessary.

## Privacy
Contact masking is best-effort. It is not a complete anonymization guarantee and should not replace secure storage or access controls.
