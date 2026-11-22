# PDF Edge Cases

PDF extraction can fail or reorder content when documents contain columns, tables, unusual fonts, or scanned pages.

## Test cases
- Single-column text PDF
- Two-column resume
- PDF with tables
- Scanned image-only PDF
- PDF with ligatures and Unicode punctuation
- Password-protected PDF

## Expected behavior
Return extracted text when reliable. Otherwise provide a specific, actionable parsing error and avoid producing a misleading score.