import os
from langchain_community.vectorstores import FAISS
from src.embeddings.embedding_model import get_embedding_model

VECTOR_DB_PATH = "data/vector_store"

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_texts(chunks, embeddings)

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    vector_store.save_local(VECTOR_DB_PATH)


def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store