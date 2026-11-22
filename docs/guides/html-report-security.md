# HTML Report Security

Escape user-controlled text before inserting it into HTML. Avoid rendering arbitrary uploaded markup or script content.

If reports are downloadable, use safe filenames and restrictive content types. Review generated HTML with inputs containing angle brackets, quotes, and script-like strings.