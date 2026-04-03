from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
import json

def generate_quiz(text):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-120b",
        temperature=0.3
    )

    prompt = f"""
    Generate 15 multiple choice questions from the text below.
    but category wise first 5 is easy then next five is modrate 
    and last five is hard 
    
    
        

    Return the response strictly in JSON format like this:

    [
        {{
            "question": "What is Machine Learning?",
            "options": [
                "A subset of AI",
                "A database system",
                "A hardware device",
                "A programming language"
            ],
            "answer": "A subset of AI",
            "topic": "Machine Learning Basics"
        }}
    ]

    Text:
    {text}
    """

    response=llm.invoke(prompt)
    try:
        quiz_data = json.loads(response.content)
    except:
        quiz_data = []

    return quiz_data