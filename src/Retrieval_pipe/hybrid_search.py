from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers import EnsembleRetriever


def create_hybrid_retriever(documents):

    # 1. CREATE BM25 RETRIEVER

    bm25_retriever = BM25Retriever.from_documents(
        documents
    )

    # Number of documents BM25 should return
    bm25_retriever.k = 3

    # 2. CREATE EMBEDDING MODEL

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 3. CREATE VECTOR STORE

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="rag_test"
    )

    # 4. CREATE VECTOR RETRIEVER

    vector_retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # 5. CREATE HYBRID RETRIEVER

    hybrid_retriever = EnsembleRetriever(
        retrievers=[
            bm25_retriever,
            vector_retriever
        ],
        weights=[
            0.5,
            0.5
        ]
    )

    return hybrid_retriever
