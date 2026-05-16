from src.rag_pipeline.rag_chain import get_rag_chain

def chat_with_pdf(query):
    """
    Retrieves context from the vector store and answers the query using the RAG pipeline.
    """
    response = get_rag_chain(query)
    return response