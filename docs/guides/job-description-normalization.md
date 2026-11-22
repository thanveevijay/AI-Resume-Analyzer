# Job Description Normalization

Normalize job descriptions before matching while preserving the original text for evidence display.

## Suggested pipeline
- Normalize whitespace and Unicode variants.
- Preserve acronyms such as SQL, NLP, and AWS.
- Split responsibilities, qualifications, and preferred skills.
- Identify repeated phrases without treating repetition as proof of importance.
- Keep a trace from each normalized phrase to its source sentence.

The normalized representation should be deterministic and testable.