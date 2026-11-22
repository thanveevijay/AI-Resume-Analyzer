# Security Notes

- Treat uploaded files as untrusted input.
- Enforce file-size and page-count limits in any web deployment.
- Store uploads outside the public web root.
- Do not execute macros or embedded content.
- Avoid logging full resume text.
- Escape user-provided content before rendering HTML.
- Keep dependencies updated and review vulnerability reports.
- Use temporary directories and remove files after processing.

The current command-line tool is local-first and does not provide authentication or multi-user storage.
