## 📚 NoteNinja AI  (RAG-Based Learning System)
An AI-powered study assistant that transforms static notes into an interactive learning experience. This system allows students to upload study material and interact with it using natural language, generate quizzes, and track performance — all powered by Retrieval-Augmented Generation (RAG).

## 📌 Overview

This project leverages LLMs + Semantic Search to create a smart learning companion. It bridges the gap between passive reading and active learning by enabling:

Context-aware question answering  

AI-generated quizzes  

Personalized performance analysis

## ✨ Key Features
📄 1. Smart Document Processing

Upload PDF notes

Extract and preprocess text

Intelligent text chunking for better retrieval

## 🔍 2. Semantic Search with RAG
Uses Hugging Face Embeddings for vector representation

Stores embeddings in FAISS Vector Database

Retrieves most relevant chunks for user queries

Enhances LLM responses with contextual grounding

## 💬 3. Chat with Notes (Natural Language QA)

Ask questions in plain English

Context-aware responses using RAG pipeline

Reduces hallucination by grounding answers in uploaded documents

## 🧠 4. AI-Powered Quiz Generation

Automatically generates MCQs from study material

Covers important concepts intelligently

Ensures better retention and self-evaluation

## 📊 5. Answer Evaluation & Feedback

Evaluates user responses using LLM

Calculates:

Score

Accuracy

Weak areas

Provides personalized feedback

## 📈 6. Performance Insights

Identifies weak topics

Tracks incorrect answers

Helps students focus on improvement areas

## ☁️ 7. Cloud Deployment
Fully deployed on Streamlit Cloud

Accessible anytime, anywhere

Scalable and user-friendly interface

# 📸 Demo

<img width="533" height="1797" alt="NoteNinja AI Complete Data Work Flow" src="https://github.com/user-attachments/assets/523a7eec-ec73-425c-be5d-5f6e0c2ea10c" />

<img width="1919" height="1134" alt="Screenshot 2026-04-02 001051" src="https://github.com/user-attachments/assets/740d05c8-128b-4d09-99e9-9033c11f2760" />

<img width="1919" height="1134" alt="Screenshot 2026-04-02 001144" src="https://github.com/user-attachments/assets/99467632-9d01-4ec0-b142-4bb44ba93ded" />

<img width="1919" height="1132" alt="Screenshot 2026-04-02 001215" src="https://github.com/user-attachments/assets/a3f76d61-babe-484a-be13-8fc7ab94d513" />

<img width="1919" height="1135" alt="Screenshot 2026-04-02 002704" src="https://github.com/user-attachments/assets/b68d13dd-3334-47fe-856e-eb54cdcdbd9d" />

<img width="1916" height="1135" alt="Screenshot 2026-04-02 002712" src="https://github.com/user-attachments/assets/f4ae9b2c-20dc-4408-9560-6f596b1ef1a4" />

<img width="1919" height="1129" alt="Screenshot 2026-04-02 185825" src="https://github.com/user-attachments/assets/22ae30ec-0706-43ab-9274-0b2b94d8c814" />

<img width="1919" height="1135" alt="Screenshot 2026-04-03 004810" src="https://github.com/user-attachments/assets/eaf6d96c-7dbc-4979-b8d4-8e6dfc4ae896"/> 

## 🛠️ Tech Stack
👨‍💻 Core Technologies:
Python,
Streamlit

🤖 AI & NLP:
LangChain,
Groq LLM API,
Hugging Face Embeddings

📦 Data Handling:
FAISS (Vector Database),
PDF Parsing Libraries

## 🔄 Workflow

1. User uploads study material (PDF)

2. System extracts and chunks text

3. Converts text into embeddings

4. Stores vectors in FAISS

5. User asks a question

6. Relevant context is retrieved

7. LLM generates accurate answer

8. Optional: Quiz generation & evaluation

## 🚀 How to Run Locally

# Clone the repository
git clone https://github.com/VisheshUnadkat13/NoteNinja-AI

# Navigate to project folder
cd NoteNinja-AI

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

## 🔑 Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_api_key_here

## 🎯 Use Cases
Students preparing for exams

Quick revision from notes

Self-assessment through quizzes

Concept-based learning

## 💡 Future Enhancements
Multi-document support
Adaptive learning paths
Integration with LMS platforms
Advanced analytics dashboard

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repo and submit a PR.

## 🌟 Final Note

This project demonstrates:

Real-world RAG pipeline implementation

Practical use of LLMs in education

Strong understanding of AI + Full-stack integration
