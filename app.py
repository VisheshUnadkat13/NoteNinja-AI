import streamlit as st
from src.utils.helpers import save_uploaded_file
from src.loaders.pdf_loader import load_pdf
from src.text_processing.text_splitter import split_text
from src.vector_db.faiss_store import create_vector_store
from src.chat.chat_with_notes import chat_with_pdf
from src.summarizer.summarizer import summerize_text
from src.quiz_generator.mcq_generator import generate_quiz
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
from src.utils.tts import generate_audio
# from src.utils.theme import apply_theme
from src.utils.pdf_generator import create_summary_pdf
from src.utils.quiz_pdf_generator import create_quiz_solution_pdf

st.set_page_config(page_title="NoteNinja AI")

# apply_theme()

st.title("📚 NoteNinja AI")

# ---------------- Upload Notes (GLOBAL) ----------------

st.sidebar.header("Upload Study Material")

uploaded_file = st.sidebar.file_uploader("Upload PDF Notes")

if uploaded_file:

    path = save_uploaded_file(uploaded_file)

    with st.spinner("Processing PDF (Applying OCR if scanned)..."):
        text = load_pdf(path)

    if not text.strip():
        st.sidebar.error("❌ Error: No text found. This PDF might be a scanned document or image-based. Please upload a standard text PDF.")
    else:
        chunks = split_text(text)
        
        if not chunks:
            st.sidebar.error("❌ Error: Could not extract valid text chunks from this PDF.")
        else:
            try:
                create_vector_store(chunks)
                st.sidebar.success("✅ Notes uploaded successfully!")
                st.session_state["notes_text"] = text
            except Exception as e:
                st.sidebar.error(f"❌ Failed to process PDF: {str(e)}")


# ---------------- Feature Selection ----------------

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Summarize", "Generate Quiz"]
)

# 👇 ADD HERE
language = st.selectbox(
    "🌐 Select Voice Language",
    ["English", "Hindi", "Gujarati"]
)

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu"
}

lang_code = lang_map[language]

# ---------------- Chat ----------------

# if menu == "Chat with Notes":
#     if "notes_text" not in st.session_state:
#         st.warning("Please upload notes first.")
#     else:
#         if st.button("Chat with Notes"):
#             query = st.text_input("Ask a question about your notes")

#             if query:

#                 response = chat_with_pdf(st.session_state["notes_text"])

#                 st.write(response)    
    # query = st.text_input("Ask a question about your notes")

    # if query:

    #     response = chat_with_pdf(query)

    #     st.write(response)


# ---------------- Summarize ----------------

if menu == "Summarize":

    if "notes_text" not in st.session_state:
        st.warning("Please upload notes first.")

    else:

        if st.button("Summarize Notes"):

            summary = summerize_text(st.session_state["notes_text"])

            st.subheader("📘 AI Generated Summary")

            st.write(summary)

            # ✅ Create PDF
            pdf_path = create_summary_pdf(summary)

            # ✅ Download Button
            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download Summary PDF",
                    data=pdf_file,
                    file_name="AI_Summary.pdf",
                    mime="application/pdf"
                )


# ---------------- Quiz ----------------

# if menu == "Generate Quiz":

#     if "notes_text" not in st.session_state:
#         st.warning("Please upload notes first.")
#     else:

#         if st.button("Create Quiz", key="create_quiz_btn"):

#             st.session_state.quiz = generate_quiz(st.session_state["notes_text"])
#             st.session_state.answers = {}
#             st.session_state.quiz_generated = True

#         if st.session_state.get("quiz_generated", False):

#             quiz = st.session_state.quiz
#             st.subheader("📝 Quiz")

#             # ---------------- QUESTIONS ----------------
#             for i, q in enumerate(quiz):

#                 st.write(f"**Q{i+1}. {q['question']}**")

#                 options = ["-- Select an answer --"] + q["options"]

#                 choice = st.radio(
#                     f"Select answer for Q{i+1}",   # ✅ unique label
#                     options,
#                     key=f"q_{i}"
#                 )

#                 if choice != "-- Select an answer --":
#                     st.session_state.answers[i] = choice

#             # ---------------- SINGLE SUBMIT BUTTON ----------------
#             if st.button("Submit Quiz", key="submit_quiz_btn"):

#                 if len(st.session_state.answers) < len(quiz):
#                     st.warning("Please answer all questions before submitting.")
#                 else:

#                     score = 0
#                     correct = 0
#                     total = len(quiz)
#                     wrong_details = []

#                     for i, q in enumerate(quiz):

#                         user_ans = st.session_state.answers[i]
#                         correct_ans = q["answer"]

#                         if user_ans == correct_ans:
#                             score += 1
#                             correct += 1
#                         else:
#                             wrong_details.append({
#                                 "q_no": i + 1,
#                                 "question": q["question"],
#                                 "your_answer": user_ans,
#                                 "correct_answer": correct_ans
#                             })

#                     accuracy = (score / total) * 100

#                     # ---------------- DASHBOARD ----------------
#                     st.header("📊 Result Dashboard")

#                     col1, col2, col3 = st.columns(3)
#                     col1.metric("Score", f"{score}/{total}")
#                     col2.metric("Accuracy", f"{accuracy:.2f}%")
#                     col3.metric("Correct Answers", correct)

#                     st.progress(int(accuracy))

#                     # ---------------- WRONG QUESTIONS ----------------
#                     if wrong_details:

#                         st.subheader("❌ Incorrect Questions")

#                         for item in wrong_details:

#                             st.markdown(f"""
#                             **Q{item['q_no']}: {item['question']}**

#                             - ❌ Your Answer: `{item['your_answer']}`
#                             - ✅ Correct Answer: `{item['correct_answer']}`
#                             """)
#                     else:
#                         st.success("🎉 Perfect Score!")

#                     # ---------------- AI ANALYSIS ----------------
#                     if wrong_details:

#                         st.subheader("🧠 AI Learning Insights")

#                         llm = ChatGroq(
#                             groq_api_key=GROQ_API_KEY,
#                             model_name="llama-3.3-70b-versatile"
#                         )

#                         prompt = f"""
#                         Student made mistakes in:

#                         {[item['question'] for item in wrong_details]}

#                         Provide:
#                         1. Concept explanation
#                         2. Why mistakes happen
#                         3. How to improve
#                         """

#                         analysis = llm.invoke(prompt)

#                         st.write(analysis.content)


#                     # ---------------- AI ANALYSIS + VOICE ----------------

#                     if wrong_details:

#                         st.subheader("🧠 AI Explanation with Voice")

#                         llm = ChatGroq(
#                             groq_api_key=GROQ_API_KEY,
#                             model_name="llama-3.3-70b-versatile"
#                         )

#                         for item in wrong_details:

#                             prompt = f"""
#                             Explain briefly (3-4 lines):

#                             Question: {item['question']}
#                             Correct Answer: {item['correct_answer']}

#                             Give simple explanation for a student.
#                             """

#                             response = llm.invoke(prompt)

#                             st.markdown(f"### 🔍 Q{item['q_no']} Explanation")
#                             st.write(response.content)

#                             # 🎤 Generate Audio
#                             audio_path = generate_audio(response.content, lang=lang_code)

#                             st.audio(audio_path)    

                   

# ---------------- Quiz ----------------

if menu == "Generate Quiz":

    if "notes_text" not in st.session_state:

        st.warning("Please upload notes first.")

    else:

        # ---------------------------------------------
        # CREATE QUIZ
        # ---------------------------------------------

        if st.button(
            "Create Quiz",
            key="create_quiz_btn"
        ):

            st.session_state.quiz = generate_quiz(
                st.session_state["notes_text"]
            )

            st.session_state.answers = {}

            st.session_state.quiz_generated = True

        # ---------------------------------------------
        # DISPLAY QUIZ
        # ---------------------------------------------

        if st.session_state.get(
            "quiz_generated",
            False
        ):

            quiz = st.session_state.quiz

            st.subheader("📝 Quiz")

            # -----------------------------------------
            # QUESTIONS
            # -----------------------------------------

            for i, q in enumerate(quiz):

                st.write(
                    f"### Q{i+1}. {q['question']}"
                )

                options = [
                    "-- Select an answer --"
                ] + q["options"]

                choice = st.radio(
                    f"Select answer for Q{i+1}",
                    options,
                    key=f"q_{i}"
                )

                if choice != "-- Select an answer --":

                    st.session_state.answers[i] = choice

            # -----------------------------------------
            # SUBMIT QUIZ
            # -----------------------------------------

            if st.button(
                "Submit Quiz",
                key="submit_quiz_btn"
            ):

                # -------------------------------------
                # VALIDATION
                # -------------------------------------

                if len(st.session_state.answers) < len(quiz):

                    st.warning(
                        "Please answer all questions before submitting."
                    )

                else:

                    # ---------------------------------
                    # LLM
                    # ---------------------------------

                    llm = ChatGroq(
                        groq_api_key=GROQ_API_KEY,
                        model_name="openai/gpt-oss-120b"
                    )

                    # ---------------------------------
                    # RESULT VARIABLES
                    # ---------------------------------

                    score = 0
                    correct = 0
                    total = len(quiz)

                    wrong_details = []

                    solutions = []

                    # ---------------------------------
                    # EVALUATE QUIZ
                    # ---------------------------------

                    for i, q in enumerate(quiz):

                        user_ans = st.session_state.answers[i]

                        correct_ans = q["answer"]

                        # -----------------------------
                        # SCORE
                        # -----------------------------

                        if user_ans == correct_ans:

                            score += 1
                            correct += 1

                        else:

                            wrong_details.append({

                                "q_no": i + 1,

                                "question": q["question"],

                                "your_answer": user_ans,

                                "correct_answer": correct_ans
                            })

                        # -----------------------------
                        # GENERATE AI SOLUTION
                        # -----------------------------

                        solution_prompt = f"""
                        Question:
                        {q['question']}

                        Options:
                        {q['options']}

                        Correct Answer:
                        {correct_ans}

                        Student Answer:
                        {user_ans}

                        Generate:
                        1. Deep concept explanation
                        2. Step-by-step solution
                        3. Formula explanation (if numerical)
                        4. Why correct answer is correct
                        5. Why other options are wrong
                        6. Easy student-friendly explanation
                        """

                        solution_response = llm.invoke(
                            solution_prompt
                        )

                        solutions.append(
                            solution_response.content
                        )

                    # ---------------------------------
                    # METRICS
                    # ---------------------------------

                    accuracy = (
                        score / total
                    ) * 100

                    # ---------------------------------
                    # DASHBOARD
                    # ---------------------------------

                    st.header("📊 Result Dashboard")

                    col1, col2, col3 = st.columns(3)

                    col1.metric(
                        "Score",
                        f"{score}/{total}"
                    )

                    col2.metric(
                        "Accuracy",
                        f"{accuracy:.2f}%"
                    )

                    col3.metric(
                        "Correct Answers",
                        correct
                    )

                    st.progress(int(accuracy))

                    # ---------------------------------
                    # WRONG ANSWERS
                    # ---------------------------------

                    if wrong_details:

                        st.subheader(
                            "❌ Incorrect Questions"
                        )

                        for item in wrong_details:

                            st.markdown(
                                f"""
                                <div style="
                                    background-color:#3a0d0d;
                                    padding:15px;
                                    border-radius:10px;
                                    margin-bottom:15px;
                                ">

                                <h5 style="color:#ff4b4b;">
                                Q{item['q_no']}
                                </h5>

                                <p>
                                <b>Question:</b>
                                {item['question']}
                                </p>

                                <p style="color:#ff6b6b;">
                                <b>Your Answer:</b>
                                {item['your_answer']}
                                </p>

                                <p style="color:#4CAF50;">
                                <b>Correct Answer:</b>
                                {item['correct_answer']}
                                </p>

                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                    else:

                        st.success(
                            "🎉 Perfect Score!"
                        )

                    # ---------------------------------
                    # AI LEARNING INSIGHTS
                    # ---------------------------------

                    if wrong_details:

                        st.subheader(
                            "🧠 AI Learning Insights"
                        )

                        prompt = f"""
                        Student made mistakes in:

                        {[item['question'] for item in wrong_details]}

                        Provide:
                        1. Concept explanation
                        2. Why mistakes happen
                        3. How to improve
                        4. Study strategy
                        """

                        analysis = llm.invoke(prompt)

                        st.write(
                            analysis.content
                        )

                    # ---------------------------------
                    # AI VOICE EXPLANATION
                    # ---------------------------------

                    if wrong_details:

                        st.subheader("🧠 AI Explanation with Voice")

                        llm = ChatGroq(
                            groq_api_key=GROQ_API_KEY,
                            model_name="openai/gpt-oss-120b"
                        )

                        for item in wrong_details:

                            prompt = f"""
                            Explain briefly (3-4 lines):

                            Question: {item['question']}
                            Correct Answer: {item['correct_answer']}

                            Give simple explanation for a student.
                            """

                            response = llm.invoke(prompt)

                            st.markdown(f"### 🔍 Q{item['q_no']} Explanation")
                            st.write(response.content)

                            # 🎤 Generate Audio
                            audio_path = generate_audio(response.content, lang=lang_code)

                            st.audio(audio_path)   

                    # ---------------------------------
                    # GENERATE PDF REPORT
                    # ---------------------------------

                    pdf_path = create_quiz_solution_pdf(
                        quiz,
                        st.session_state.answers,
                        solutions
                    )

                    # ---------------------------------
                    # DOWNLOAD PDF
                    # ---------------------------------

                    with open(pdf_path, "rb") as pdf_file:

                        st.download_button(
                            label="📥 Download Full Solution PDF",
                            data=pdf_file,
                            file_name="AI_Quiz_Solutions.pdf",
                            mime="application/pdf",
                            key="download_solution_pdf"
                        )                   