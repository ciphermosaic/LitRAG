from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def create_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vectorstore(documents):
    embeddings = create_embeddings()

    return Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="rag_test"
    )