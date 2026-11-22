# Output Schema

A report includes:
- `generated_at`: UTC timestamp.
- `comparison`: detected resume/job skills, matched and missing skills, plus optional evidence.
- `score`: heuristic coverage value, counts, method, and interpretation.
- `recommendations`: evidence-based suggestions.
- `disclaimer`: reminder that the result is not an automated hiring decision.

Consumers should tolerate additional fields in future versions and must not interpret a missing skill as proof that a candidate lacks it.
