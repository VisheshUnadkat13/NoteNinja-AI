# from src.rag_pipeline.rag_chain import get_rag_chain


# def chat_with_pdf(query):

#     response = get_rag_chain(query)

#     return response


from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

def chat_with_pdf(query):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        temperature=0.5,
        model_name="llama-3.3-70b-versatile"
    )

    prompt=f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response=llm.invoke(prompt)
    return response.content