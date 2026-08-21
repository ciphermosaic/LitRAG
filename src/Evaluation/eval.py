#METRICS...........................

def evaluate_retriever(retriever, evaluation_data, k=5): #give dataset in evaluation_data feild

    precision_scores = []
    recall_scores = []
    hit_rates = []
    reciprocal_ranks = []

    for item in evaluation_data:

        query = item["question"]
        relevant = item["relevant"]

        results = retriever.invoke(query)

        retrieved = [
            doc.metadata["id"]
            for doc in results[:k]
        ]

        # Relevant documents retrieved
        relevant_retrieved = sum(
            1
            for doc_id in retrieved
            if doc_id in relevant
        )

        # Precision@K
        precision = relevant_retrieved / k

        # Recall@K
        recall = relevant_retrieved / len(relevant)

        # Hit Rate@K
        hit_rate = int(
            any(doc_id in relevant for doc_id in retrieved)
        )

        # MRR
        reciprocal_rank = 0

        for rank, doc_id in enumerate(retrieved, start=1):

            if doc_id in relevant:
                reciprocal_rank = 1 / rank
                break

        precision_scores.append(precision)
        recall_scores.append(recall)
        hit_rates.append(hit_rate)
        reciprocal_ranks.append(reciprocal_rank)

    print("Precision@K :", sum(precision_scores) / len(precision_scores))
    print("Recall@K    :", sum(recall_scores) / len(recall_scores))
    print("Hit Rate@K  :", sum(hit_rates) / len(hit_rates))
    print("MRR         :", sum(reciprocal_ranks) / len(reciprocal_ranks))


from .llm import llm

def llm_as_judge(question, context, answer):
    prompt = f"""
    You are an evaluator for a RAG system.

    Question:
    {question}

    Context:
    {context}

    Answer:
    {answer}

    Evaluate the answer based on the context.

    Give a score from 0 to 1:
    1 = completely supported by the context
    0 = completely unsupported

    Return only the score.
    """

    result = llm.invoke(prompt)

    return float(result.content.strip())
