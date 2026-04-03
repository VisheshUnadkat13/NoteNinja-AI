from langchain_groq import ChatGroq
from src.vector_db.faiss_store import load_vector_store
from config.settings import GROQ_API_KEY

def get_rag_chain(query):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever()

    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0.2
    )

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content   