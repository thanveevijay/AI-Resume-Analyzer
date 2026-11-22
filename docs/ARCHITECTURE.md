# Architecture

The pipeline follows a sequence of small, testable modules:

1. **Extraction** converts supported files into text.
2. **Validation** rejects missing or insufficient inputs.
3. **Normalization** standardizes case and punctuation.
4. **Matching** detects taxonomy terms in resume and job text.
5. **Evidence** returns short sentences supporting detected matches.
6. **Scoring** calculates a transparent skill coverage ratio.
7. **Recommendations** suggests evidence-based edits for missing terms.
8. **Reporting** serializes results as JSON or safe HTML.

Each stage is deterministic for a fixed input, except the report timestamp.
