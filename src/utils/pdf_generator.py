import os
import re
from datetime import datetime
from fpdf import FPDF

SUMMARY_FOLDER = "data/summaries"


# ---------------------------------------------------
# CLEAN TEXT FUNCTION
# ---------------------------------------------------

def clean_text(text):

    replacements = {

        "–": "-",
        "—": "-",
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "•": "*",
        "→": "->",
        "✓": "[OK]",
        "❌": "[X]",
        "✅": "[OK]"
    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    # Remove unsupported unicode
    text = re.sub(
        r'[^\x00-\x7F]+',
        ' ',
        text
    )

    return text


# ---------------------------------------------------
# CREATE SUMMARY PDF
# ---------------------------------------------------

def create_summary_pdf(summary_text):

    os.makedirs(
        SUMMARY_FOLDER,
        exist_ok=True
    )

    # Clean Text
    summary_text = clean_text(summary_text)

    # Unique File Name
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    output_path = (
        f"{SUMMARY_FOLDER}/summary_{timestamp}.pdf"
    )

    # Create PDF
    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.add_page()

    # Title
    pdf.set_font(
        "Arial",
        style='B',
        size=18
    )

    pdf.cell(
        200,
        10,
        "AI Generated Summary",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    # Content
    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.multi_cell(
        0,
        8,
        summary_text
    )

    # Save PDF
    pdf.output(output_path)

    return output_path