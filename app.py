import streamlit as st
from src.utils.helpers import save_uploaded_file
from src.loaders.pdf_loader import load_pdf
from src.loaders.image_loader import load_image
from src.loaders.ppt_loader import load_pptx
from src.text_processing.text_splitter import split_text
from src.vector_db.faiss_store import create_vector_store
from src.chat.chat_with_notes import chat_with_pdf
from src.summarizer.summarizer import summerize_text
from src.quiz_generator.mcq_generator import generate_quiz
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
from src.utils.tts import generate_audio
from src.utils.theme import apply_theme
from src.utils.pdf_generator import create_summary_pdf
from src.utils.quiz_pdf_generator import create_quiz_solution_pdf
from src.utils.youtube_search import search_youtube_videos

st.set_page_config(page_title="NoteNinja AI", layout="wide", initial_sidebar_state="expanded")

apply_theme()

# Hero Section
st.markdown("""
    <div class="hero-section" style="text-align: center; padding: 60px 0px 40px 0px;">
        <h1 style="font-size: 4.5rem; margin-bottom: 20px; line-height: 1.1;">📚 NoteNinja AI</h1>
        <p style="font-size: 1.4rem; color: #94a3b8; max-width: 700px; margin: 0 auto; line-height: 1.6;">
            The ultimate AI-powered study companion. Upload your notes and let NoteNinja transform them into professional summaries and interactive quizzes.
        </p>
    </div>
""", unsafe_allow_html=True)

# ---------------- Upload Notes (GLOBAL) ----------------

st.sidebar.header("Upload Study Material")

uploaded_file = st.sidebar.file_uploader(
    "Upload Notes (PDF, PPTX, Images)", 
    type=["pdf", "pptx", "png", "jpg", "jpeg"]
)

if uploaded_file:

    path = save_uploaded_file(uploaded_file)
    ext = uploaded_file.name.split(".")[-1].lower()

    with st.spinner(f"Processing {ext.upper()} (Applying OCR if needed)..."):
        if ext == "pdf":
            text = load_pdf(path)
        elif ext == "pptx":
            text = load_pptx(path)
        elif ext in ["png", "jpg", "jpeg"]:
            text = load_image(path)
        else:
            text = ""

    if not text.strip():
        st.sidebar.error("❌ Error: No text found. Please ensure the file contains readable content.")
    else:
        chunks = split_text(text)
        
        if not chunks:
            st.sidebar.error("❌ Error: Could not extract valid text chunks from this file.")
        else:
            try:
                create_vector_store(chunks)
                st.sidebar.success("✅ Notes uploaded successfully!")
                st.session_state["notes_text"] = text
            except Exception as e:
                st.sidebar.error(f"❌ Failed to process file: {str(e)}")


# ---------------- Feature Selection ----------------
st.sidebar.markdown("---")
st.sidebar.markdown("### 🛠️ Workspace")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Chat with Notes","Summarize", "Generate Quiz", "Video Recommendations"]
)

# 👇 Voice Settings
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔊 Voice Settings")
language = st.sidebar.selectbox(
    "Select Voice Language",
    ["English", "Hindi", "Gujarati"]
)

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu"
}

lang_code = lang_map[language]

# ---------------- Chat ----------------

if menu == "Chat with Notes":
    if "notes_text" not in st.session_state:
        st.markdown("""
            <div class="premium-card" style="text-align: center; padding: 50px;">
                <h2 style="margin-bottom: 20px;">Chat with Your Knowledge</h2>
                <p style="font-size: 1.1rem; color: #94a3b8; margin-bottom: 30px;">
                    Upload your notes in the sidebar to start a conversation with NoteNinja AI.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 💬 Chat with Your Notes")
        st.write("Ask anything about your uploaded study material.")
        
        query = st.text_input("Type your question here...", key="chat_query")

        if query:
            with st.spinner("NoteNinja is thinking..."):
                try:
                    response = chat_with_pdf(query)
                    st.markdown("---")
                    st.markdown(f"**🤖 NoteNinja:** {response}")
                except Exception as e:
                    st.error(f"❌ Error during chat: {str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)


# ---------------- Summarize ----------------

if menu == "Summarize":

    if "notes_text" not in st.session_state:
        st.markdown("""
            <div class="premium-card" style="text-align: center; padding: 50px;">
                <h2 style="margin-bottom: 20px;">Ready to Start?</h2>
                <p style="font-size: 1.1rem; color: #94a3b8; margin-bottom: 30px;">
                    Upload a document (PDF, PPTX, or Image) in the sidebar to unlock the power of AI summarization.
                </p>
                <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                    <div style="background: rgba(99, 102, 241, 0.1); padding: 20px; border-radius: 16px; border: 1px solid rgba(99, 102, 241, 0.2); width: 200px;">
                        <h3 style="font-size: 1.2rem; margin-bottom: 10px;">✨ Smart Summaries</h3>
                        <p style="font-size: 0.9rem; color: #94a3b8;">Get the core concepts without the fluff.</p>
                    </div>
                    <div style="background: rgba(168, 85, 247, 0.1); padding: 20px; border-radius: 16px; border: 1px solid rgba(168, 85, 247, 0.2); width: 200px;">
                        <h3 style="font-size: 1.2rem; margin-bottom: 10px;">🎧 Voice Output</h3>
                        <p style="font-size: 0.9rem; color: #94a3b8;">Listen to explanations in multiple languages.</p>
                    </div>
                    <div style="background: rgba(139, 92, 246, 0.1); padding: 20px; border-radius: 16px; border: 1px solid rgba(139, 92, 246, 0.2); width: 200px;">
                        <h3 style="font-size: 1.2rem; margin-bottom: 10px;">📄 PDF Export</h3>
                        <p style="font-size: 0.9rem; color: #94a3b8;">Download and keep your AI-generated notes.</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Summarize Your Notes")
        st.write("Get a concise summary of your uploaded document in seconds.")
        
        if st.button("✨ Summarize Now"):

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
        st.markdown('</div>', unsafe_allow_html=True)


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
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Generate a Smart Quiz")
        st.write("Test your knowledge with AI-generated multiple-choice questions.")

        if st.button(
            "🚀 Create My Quiz",
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
            
            st.markdown('</div>', unsafe_allow_html=True)

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

                    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
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
                    st.markdown('</div>', unsafe_allow_html=True)

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
                                <div class="premium-card" style="border-left: 5px solid #ff4b4b;">
                                    <h5 style="color:#ff4b4b; margin-top: 0;">Q{item['q_no']}</h5>
                                    <p><b>Question:</b> {item['question']}</p>
                                    <p style="color:#ff6b6b;"><b>Your Answer:</b> {item['your_answer']}</p>
                                    <p style="color:#4CAF50;"><b>Correct Answer:</b> {item['correct_answer']}</p>
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
                        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
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
                        st.markdown('</div>', unsafe_allow_html=True)

                    # ---------------------------------
                    # AI VOICE EXPLANATION
                    # ---------------------------------

                    if wrong_details:
                        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
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
                        st.markdown('</div>', unsafe_allow_html=True)

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

# ---------------- Video Recommendations ----------------

if menu == "Video Recommendations":
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("### 🎥 Video Recommendations")
    st.write("Get hand-picked YouTube videos to master any topic.")
    
    # Use the session state notes text as a default search query if available
    default_query = ""
    if "notes_text" in st.session_state:
        # Try to get a good search term from the notes if possible, otherwise leave empty
        # For now, let's just let the user type.
        pass
        
    search_query = st.text_input("Enter topic to search videos for:", placeholder="e.g., OOPS Concepts in Java", key="youtube_search_input")
    
    if st.button("🔍 Find Videos", key="search_videos_btn"):
        if search_query:
            with st.spinner(f"Searching for '{search_query}' videos..."):
                videos = search_youtube_videos(search_query)
                
                if videos:
                    st.markdown("---")
                    st.subheader(f"📺 Top Recommendations for '{search_query}'")
                    
                    for video in videos:
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            st.image(video['thumbnail'], use_container_width=True)
                        
                        with col2:
                            st.markdown(f"#### {video['title']}")
                            st.markdown(f"**Channel:** {video['channel']}")
                            st.markdown(f"**Duration:** {video['duration']} | **Views:** {video['views']}")
                            st.markdown(f'''
                                <a href="{video['link']}" target="_blank">
                                    <button style="
                                        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                                        color: white;
                                        border: none;
                                        padding: 8px 16px;
                                        border-radius: 8px;
                                        cursor: pointer;
                                        font-weight: 600;
                                    ">Watch on YouTube ↗</button>
                                </a>
                            ''', unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                else:
                    st.warning("No videos found. Please try a different search term.")
        else:
            st.error("Please enter a topic to search.")
    st.markdown('</div>', unsafe_allow_html=True)
                 