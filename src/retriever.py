from .hybrid_search import create_hybrid_retriever
def create_retriever(documents):

    hybrid_retriever = create_hybrid_retriever(
        documents
    )

    return hybrid_retriever