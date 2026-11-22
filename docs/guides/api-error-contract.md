# API Error Contract

Return structured errors with a stable code, human-readable message, and optional field identifier.

Expected categories include unsupported file type, unreadable document, empty extracted text, invalid job description, and internal processing failure.

Do not include raw resume text, stack traces, or personal data in client-facing errors.