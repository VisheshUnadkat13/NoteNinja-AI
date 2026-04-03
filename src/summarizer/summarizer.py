from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

def summerize_text(text):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-120b",
        temperature=0.5
    )

    prompt=f"""
    summerize this content in bullet points:
    summerize every topic clearly and in detail:
    
    {text}
    """

    response=llm.invoke(prompt)
    return response.content