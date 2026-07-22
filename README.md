## Architecture

<img width="1536" height="1024" alt="NoteNinja AI DataFlow Diagrma" src="https://github.com/user-attachments/assets/3d56b620-8c70-40a0-be19-58561ff54371" />


## 1.  CHAT WITH NOTE MODULE - DATAFLOW DIAGRAM

<img width="3000" height="1300" alt="chat_with_note_module_dataflow" src="https://github.com/user-attachments/assets/ea3726e2-a2a3-47fc-9998-d6b86e33b971" />


## 2.  SUMMERY MODULE - DATAFLOW DIAGRAM

<img width="3000" height="1240" alt="summary_module_dataflow" src="https://github.com/user-attachments/assets/dfc9b8c6-3c89-480e-b74c-41fe78d55f72" />


## 3. QUIZ GENERATION MODULE - DATAFLOW DIAGRAM

<img width="3000" height="1240" alt="quiz_generation_module_dataflow" src="https://github.com/user-attachments/assets/cd976097-b6de-40a8-8459-b73ae524c8b9" />

## Screenshots
<img width="1918" height="1033" alt="Screenshot 2026-07-02 134412" src="https://github.com/user-attachments/assets/c78750f0-1221-4c5e-a0c1-d7b9d1776e4e" />
<img width="1918" height="1035" alt="Screenshot 2026-07-02 134532" src="https://github.com/user-attachments/assets/3d795ac4-dee7-408b-b4b8-63522730558a" />
<img width="1917" height="1031" alt="Screenshot 2026-07-02 134544" src="https://github.com/user-attachments/assets/bb42ed9b-8b81-462c-950e-ec943332df65" />
<img width="1918" height="1032" alt="Screenshot 2026-07-02 134557" src="https://github.com/user-attachments/assets/4f7f0e84-9748-48af-8fcc-63926dea1497" />
<img width="1918" height="1026" alt="Screenshot 2026-07-02 134615" src="https://github.com/user-attachments/assets/23154dd1-05cd-40d6-879b-d32d8883be2d" />
<img width="1918" height="1026" alt="Screenshot 2026-07-02 134630" src="https://github.com/user-attachments/assets/495794e9-9985-416f-b61b-c3f9d4597db9" />
<img width="1918" height="1030" alt="Screenshot 2026-07-02 134640" src="https://github.com/user-attachments/assets/42023d8d-09d8-4ab9-aa5c-e41d5c2c78d5" />
<img width="1918" height="1025" alt="Screenshot 2026-07-02 134906" src="https://github.com/user-attachments/assets/29044096-94c0-466c-a9c4-7e925e023740" />
<img width="1918" height="1020" alt="Screenshot 2026-07-02 135723" src="https://github.com/user-attachments/assets/1f7a26c7-8fcf-46b5-a52c-7ee051be2a09" />
<img width="1918" height="1027" alt="Screenshot 2026-07-02 135929" src="https://github.com/user-attachments/assets/66d7201a-5134-4192-9241-1bad0aab7af5" />
<img width="1918" height="1027" alt="Screenshot 2026-07-02 135939" src="https://github.com/user-attachments/assets/85945a64-3172-4c2f-9b46-782cb9058995" />
<img width="1918" height="1025" alt="Screenshot 2026-07-02 135958" src="https://github.com/user-attachments/assets/092ccab4-d86f-4fae-a3a5-02a0a69a6d82" />



# 📚 NoteNinja AI 

---

## 🚀 Project Overview

* AI-powered study assistant to **chat with notes, generate quizzes, and analyze performance**
* Built using **RAG (Retrieval-Augmented Generation)** architecture
* Converts static PDFs into an **interactive AI learning system**

---

## Live Project Link : https://noteninja-ai.streamlit.app/

## 🧠 Core Features

* 📄 Upload PDF and extract structured text
* 💬 Chat with notes using semantic search + LLM
* 📝 Generate MCQ-based quizzes from notes
* 📊 AI-powered result dashboard (score, accuracy, weak areas)
* ❌ Question-level mistake tracking (wrong question no + correct answer)
* 🧠 AI-generated explanation for each wrong answer
* 🎤 Multilingual voice explanation (English, Hindi, Gujarati)
* 🌙 Dark/Light mode UI toggle

---

## 🏗️ Workflow (End-to-End)

* Upload PDF
* Extract text → split into chunks
* Convert chunks → embeddings
* Store in FAISS vector DB
* User query → semantic retrieval
* Send context → LLM (Groq)
* Generate:

  * Answer (chat)
  * Quiz
  * Explanation
* Evaluate quiz → generate dashboard + insights
* Convert explanation → voice output

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend / AI**: LangChain, Groq API
* **Embeddings**: Hugging Face (`all-MiniLM-L6-v2`)
* **Vector DB**: FAISS
* **LLMs Used**:

  * `llama-3.3-70b-versatile` (tested)
  * `openai/gpt-oss-120b`  ✅ (final)
* **TTS (Voice)**: Hugging Face MMS-TTS

---

## ⚡ Key Technical Decisions

* Replaced **Ollama embeddings → HuggingFace embeddings** for cloud compatibility
* Selected **MiniLM model** for fast CPU inference + deployment stability
* Used **Groq LLM** for ultra-fast response generation
* Implemented **session state management** for quiz tracking

---

## 🚨 Challenges Faced & Solutions

### ❌ Ollama Not Working in Deployment

* Problem: Local models not supported in Streamlit Cloud
* Solution: Switched to HuggingFace embeddings

---

### ❌ FAISS IndexError (Empty Embeddings)

* Problem: Empty chunks → crash
* Solution:

  * Added validation for text & chunks
  * Filtered empty inputs

---

### ❌ LLM Selection & Performance

* Problem: Trade-off between speed & accuracy
* Solution:

  * Tested multiple models
  * Finalized `openai/gpt-oss-120b`

---

### ❌ Multilingual Voice Issue

* Problem: TTS requires language-specific input
* Solution:

  * Generated response in target language
  * Then passed to TTS

---

### ❌ Streamlit UI Issues

* Problem:

  * Default selected options
  * Duplicate button errors
* Solution:

  * Placeholder options
  * Unique keys
  * Controlled session state

---

### ❌ GitHub Push Protection Error

* Problem: API key exposed
* Solution:

  * Removed `.env` from repo
  * Used `.gitignore`
  * Configured Streamlit secrets

---

## 📊 AI Dashboard Features

* Score calculation
* Accuracy percentage
* Correct vs incorrect answers
* Weak topic identification
* Question-wise mistake analysis
* AI-generated improvement suggestions

---

## 🎤 Advanced Feature

* AI-generated **voice explanation for wrong answers**
* Multilingual support:

  * English
  * Hindi
  * Gujarati
* Implemented using Hugging Face TTS models

---

## 🚀 Deployment

* Platform: Streamlit Cloud
* Key changes:

  * Removed local dependencies
  * Used lightweight models
  * Secured API keys via secrets

---

## 💼 Resume Highlights

* Built end-to-end **AI-powered RAG application**
* Integrated **LLM + Vector DB + Voice AI**
* Designed **quiz evaluation + analytics system**
* Solved real-world **deployment & scaling challenges**

---

## 🔮 Future Improvements

* User authentication
* Progress tracking
* Multi-user SaaS version
* Real-time voice interaction

---

## ⭐ Final Output

* Fully working **AI Study Platform**
* Combines:

  * RAG
  * LLM
  * Voice AI
  * Analytics

---
## 🔗 Links
[![DantaVaidya – AI](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://noteninja-ai.streamlit.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishesh-unadkat/)
