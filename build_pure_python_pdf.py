"""
Enhanced Pure Python PDF Generator for Launch_Kit.pdf
Cleans unicode artifacts and formats tables with clean tabular alignment.
"""

import os
import re
from pathlib import Path

WORKSPACE_DIR = str(Path(__file__).resolve().parent)
MD_PATH = os.path.join(WORKSPACE_DIR, "Launch_Kit", "Launch_Kit.md")
PDF_PATH = os.path.join(WORKSPACE_DIR, "Launch_Kit", "Launch_Kit.pdf")

def clean_unicode(text):
    # Replace typography chars with clean ASCII
    replacements = {
        '–': '-',
        '—': ' - ',
        '“': '"',
        '”': '"',
        '’': "'",
        '‘': "'",
        '…': '...',
        '→': '->',
        '•': '*',
        '>=': '>=',
        '<=': '<=',
        '✓': '[x]',
        '✗': '[ ]'
    }
    for orig, rep in replacements.items():
        text = text.replace(orig, rep)
    return text.encode('latin-1', 'replace').decode('latin-1')

def generate_clean_pdf(lines, output_path):
    pages_streams = []
    current_stream = []
    y = 740

    for line in lines:
        line_clean = clean_unicode(line.strip())
        if not line_clean:
            y -= 14
            if y < 60:
                pages_streams.append(current_stream)
                current_stream = []
                y = 740
            continue

        # Skip horizontal dividers and mermaid block syntax
        if line_clean.startswith("---") or line_clean.startswith("```") or line_clean in ["mermaid", "flowchart TD"]:
            continue

        # Detect headers
        if line_clean.startswith("# "):
            font = "/F2 16"
            dy = 22
            text = line_clean[2:]
        elif line_clean.startswith("## "):
            font = "/F2 13"
            dy = 18
            text = line_clean[3:]
        elif line_clean.startswith("### "):
            font = "/F2 11"
            dy = 15
            text = line_clean[4:]
        elif line_clean.startswith("|"):
            # Table formatting
            if "---" in line_clean:
                continue
            font = "/F1 8"
            dy = 13
            # Clean and space table cells
            cells = [c.strip() for c in line_clean.strip('|').split('|')]
            text = "  |  ".join(cells)
        else:
            font = "/F1 9"
            dy = 12
            text = line_clean

        # Clean markdown formatting
        text = re.sub(r'[*_`#\[\]]', '', text)
        text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

        # Word wrap (approx 90 chars per line for /F1 9)
        max_chars = 90 if "/F1" in font else 70
        words = text.split(' ')
        wrapped_lines = []
        cur_line = []
        cur_len = 0
        for w in words:
            if cur_len + len(w) + 1 > max_chars:
                wrapped_lines.append(' '.join(cur_line))
                cur_line = [w]
                cur_len = len(w)
            else:
                cur_line.append(w)
                cur_len += len(w) + 1
        if cur_line:
            wrapped_lines.append(' '.join(cur_line))

        for wl in wrapped_lines:
            if y < 60:
                pages_streams.append(current_stream)
                current_stream = []
                y = 740
            font_name, font_size = font.split()
            stream_cmd = f"BT {font_name} {font_size} Tf 50 {y} Td ({wl}) Tj ET"
            current_stream.append(stream_cmd)
            y -= dy

    if current_stream:
        pages_streams.append(current_stream)

    num_pages = len(pages_streams)
    catalog_id = 1
    pages_id = 2
    first_page_id = 3
    first_content_id = first_page_id + num_pages
    font_f1_id = first_content_id + num_pages
    font_f2_id = font_f1_id + 1

    page_ids = [first_page_id + i for i in range(num_pages)]
    content_ids = [first_content_id + i for i in range(num_pages)]

    pdf_parts = []
    pdf_parts.append("%PDF-1.4\n")
    offsets = {}

    def add_obj(obj_id, body):
        offsets[obj_id] = sum(len(p.encode('latin-1')) for p in pdf_parts)
        pdf_parts.append(f"{obj_id} 0 obj\n{body}\nendobj\n")

    add_obj(catalog_id, f"<< /Type /Catalog /Pages {pages_id} 0 R >>")
    kids_str = " ".join(f"{pid} 0 R" for pid in page_ids)
    add_obj(pages_id, f"<< /Type /Pages /Kids [{kids_str}] /Count {num_pages} >>")

    for i in range(num_pages):
        pid = page_ids[i]
        cid = content_ids[i]
        page_body = f"""<< /Type /Page
/Parent {pages_id} 0 R
/MediaBox [0 0 612 792]
/Contents {cid} 0 R
/Resources <<
  /Font <<
    /F1 {font_f1_id} 0 R
    /F2 {font_f2_id} 0 R
  >>
>>
>>"""
        add_obj(pid, page_body)

    for i in range(num_pages):
        cid = content_ids[i]
        stream_content = "\n".join(pages_streams[i])
        stream_bytes = stream_content.encode('latin-1')
        stream_body = f"<< /Length {len(stream_bytes)} >>\nstream\n{stream_content}\nendstream"
        add_obj(cid, stream_body)

    add_obj(font_f1_id, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    add_obj(font_f2_id, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    xref_offset = sum(len(p.encode('latin-1')) for p in pdf_parts)
    total_objects = font_f2_id + 1

    xref_str = f"xref\n0 {total_objects}\n0000000000 65535 f \n"
    for i in range(1, total_objects):
        xref_str += f"{offsets[i]:010d} 00000 n \n"

    trailer_str = f"trailer\n<< /Size {total_objects} /Root {catalog_id} 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"
    pdf_parts.append(xref_str)
    pdf_parts.append(trailer_str)

    with open(output_path, "wb") as f:
        f.write("".join(pdf_parts).encode('latin-1'))

    print(f"SUCCESS: Generated clean {output_path} with {num_pages} pages ({os.path.getsize(output_path)} bytes).")

if __name__ == "__main__":
    with open(MD_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    generate_clean_pdf(lines, PDF_PATH)
