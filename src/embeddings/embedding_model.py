# from langchain_community.embeddings import OllamaEmbeddings

# def get_embeddings():
#     return OllamaEmbeddings(model="nomic-embed-text")


from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return model
