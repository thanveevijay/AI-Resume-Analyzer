# Regression Test Matrix

| Area | Regression scenario | Expected result |
|---|---|---|
| Extraction | Empty PDF | Clear validation error |
| Matching | Case variation | Same normalized match |
| Matching | Negated skill mention | No unsupported positive evidence |
| Scoring | No required skills | Safe zero/undefined handling |
| Reporting | Special characters | Valid JSON and escaped HTML |
| Privacy | Contact details | Redacted in diagnostics |

Add a regression test whenever a parsing or scoring defect is fixed.