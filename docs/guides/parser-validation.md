# Parser Validation

## Purpose
Verify that uploaded resume content is extracted consistently before scoring.

## Checks
- Confirm the file type is supported before parsing.
- Reject empty or whitespace-only extracted text.
- Preserve section headings and bullet boundaries where possible.
- Record parser warnings separately from scoring results.
- Test multi-column PDFs and scanned documents explicitly.

## Acceptance criteria
A parse is usable only when meaningful text is present and the user can inspect the extracted content. Scanned PDFs should receive a clear OCR limitation message.