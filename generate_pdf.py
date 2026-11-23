"""
Converts Launch_Kit.md to a beautifully styled PDF using Microsoft Edge headless.
"""

import os
import subprocess
import re

from pathlib import Path
WORKSPACE_DIR = str(Path(__file__).resolve().parent)
MD_PATH = os.path.join(WORKSPACE_DIR, "Launch_Kit", "Launch_Kit.md")
HTML_PATH = os.path.join(WORKSPACE_DIR, "Launch_Kit", "Launch_Kit.html")
PDF_PATH = os.path.join(WORKSPACE_DIR, "Launch_Kit", "Launch_Kit.pdf")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert basic markdown elements to HTML
html_body = md_text
# Convert headers
html_body = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_body, flags=re.MULTILINE)

# Bold & italics
html_body = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_body)
html_body = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_body)

# Tables (simple conversion)
lines = html_body.split('\n')
in_table = False
table_html = []
final_lines = []

for line in lines:
    if line.strip().startswith('|') and line.strip().endswith('|'):
        if not in_table:
            in_table = True
            final_lines.append('<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse; width:100%; margin:16px 0;">')
        if '---' in line:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        row_tag = 'th' if not table_html else 'td'
        table_html.append('<tr>' + ''.join(f'<{row_tag}>{c}</{row_tag}>' for c in cells) + '</tr>')
        final_lines.append(table_html[-1])
    else:
        if in_table:
            in_table = False
            final_lines.append('</table>')
            table_html = []
        final_lines.append(line)

html_content = '\n'.join(final_lines)

styled_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>IncuBrix 90-Day Growth & Visibility Launch Kit</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1F2937;
    line-height: 1.6;
    margin: 40px;
    font-size: 13px;
  }}
  h1 {{ color: #1E3A8A; font-size: 26px; border-bottom: 2px solid #E5E7EB; padding-bottom: 8px; }}
  h2 {{ color: #1E40AF; font-size: 18px; margin-top: 24px; border-bottom: 1px solid #E5E7EB; padding-bottom: 4px; }}
  h3 {{ color: #374151; font-size: 15px; margin-top: 18px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 12px; }}
  th {{ background-color: #F3F4F6; color: #1F2937; text-align: left; padding: 8px; border: 1px solid #D1D5DB; }}
  td {{ padding: 8px; border: 1px solid #E5E7EB; vertical-align: top; }}
  tr:nth-child(even) {{ background-color: #F9FAFB; }}
  blockquote {{ border-left: 4px solid #3B82F6; padding-left: 12px; margin: 16px 0; color: #4B5563; font-style: italic; }}
  code {{ background-color: #F3F4F6; padding: 2px 4px; border-radius: 4px; font-family: Consolas, monospace; font-size: 11px; }}
</style>
</head>
<body>
{html_content}
</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(styled_html)

# Run Edge headless print-to-pdf
cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={PDF_PATH}",
    HTML_PATH
]

print("Printing PDF using Edge headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(PDF_PATH):
    print(f"SUCCESS: Created {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")
else:
    print(f"Edge print-to-pdf finished with code {res.returncode}. Output: {res.stdout} {res.stderr}")
