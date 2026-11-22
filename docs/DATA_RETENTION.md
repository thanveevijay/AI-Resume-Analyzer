# Data Retention

The CLI reads files locally and does not intentionally persist their contents. If a web interface or hosted API is added, define a retention policy before launch.

Recommended defaults:
- Process uploads in a temporary location.
- Delete temporary files after the request completes.
- Do not retain reports unless the user explicitly exports them.
- Provide deletion controls for any persisted account data.
- Avoid storing resume text in analytics and error logs.
