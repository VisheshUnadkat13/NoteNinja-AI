import os
from datetime import datetime
from fpdf import FPDF

QUIZ_REPORT_FOLDER = "data/quiz_reports"


def create_quiz_solution_pdf(quiz, user_answers, solutions):

    os.makedirs(QUIZ_REPORT_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_path = f"{QUIZ_REPORT_FOLDER}/quiz_report_{timestamp}.pdf"

    pdf = FPDF()

    pdf.add_page()

    # Title
    pdf.set_font("Arial", style='B', size=18)

    pdf.cell(
        200,
        10,
        "AI Quiz Solution Report",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    for i, q in enumerate(quiz):

        # Unicode safe
        question = q["question"].encode(
            "latin-1",
            "replace"
        ).decode("latin-1")

        correct_answer = q["answer"].encode(
            "latin-1",
            "replace"
        ).decode("latin-1")

        user_answer = user_answers[i].encode(
            "latin-1",
            "replace"
        ).decode("latin-1")

        solution = solutions[i].encode(
            "latin-1",
            "replace"
        ).decode("latin-1")

        # Question
        pdf.set_font("Arial", style='B', size=14)

        pdf.multi_cell(
            0,
            10,
            f"Q{i+1}: {question}"
        )

        pdf.ln(2)

        # User Answer
        pdf.set_font("Arial", size=12)

        pdf.multi_cell(
            0,
            8,
            f"Your Answer: {user_answer}"
        )

        # Correct Answer
        pdf.multi_cell(
            0,
            8,
            f"Correct Answer: {correct_answer}"
        )

        pdf.ln(2)

        # Solution
        pdf.set_font("Arial", style='B', size=12)

        pdf.cell(0, 8, "Detailed Explanation:", ln=True)

        pdf.set_font("Arial", size=12)

        pdf.multi_cell(
            0,
            8,
            solution
        )

        pdf.ln(10)

    pdf.output(output_path)

    return output_path