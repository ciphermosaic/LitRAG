from sentence_transformers import CrossEncoder

def reranker(query, retriever):
    #1. retrieve docs
    retrieved_docs = retriever.invoke(query)

    #2. Load Reranker
    reranker = CrossEncoder("cross-encoder/ms-msa-all-MiniLM-L-6-v2")

    #3. Create (query, documents) pairs
    pairs = [(query, doc.page_content) for doc in retrieved_docs]

    #4. Calculate relevance scores
    scores = reranker.predict(pairs)

    #5. combine scores and sort
    ranked_docs = sorted(zip(retrieved_docs, scores), key=lambda x:x[1], reverse=True)

    #6. keep top docs
    top_docs = (doc for doc, scores in ranked_docs)

    #7. create context
    context = "\n\n".join(doc.page_content for doc in top_docs)

    return context
