# Privacy Threat Model

## Assets
Resume documents, extracted text, contact details, job descriptions, and generated reports.

## Threats
Unauthorized access, accidental logging, insecure temporary files, unsafe HTML rendering, and unintended data retention.

## Mitigations
- Process only the information required for analysis.
- Keep uploaded documents out of application logs.
- Restrict access to generated reports.
- Escape user-controlled content in HTML output.
- Remove temporary files after processing.
- Document retention and deletion behavior before enabling persistence.