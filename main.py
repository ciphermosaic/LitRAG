from Ingestion_pipe.pipeline import ingest
from Retriever_pipe.retriever import create_retriever
from Retriever_pipe.query_rewriting import rewrite_query
from Retriever_pipe.reranker import reranker
from Evaluation.llm import llm


def main():
    # 1. INGEST RESEARCH PAPER

    file_path = "data/pdfs"

    documents = ingest(file_path)

    print("\nIngestion completed successfully.")

    # 2. CREATE HYBRID RETRIEVER

    retriever = create_retriever(documents)

    print("Hybrid retriever created successfully.")

    # 3. QUESTION LOOP

    while True:

        query = input(
            "\nAsk a question (type 'exit' to quit): "
        )

        if query.lower() == "exit":
            break

        if not query.strip():
            continue

        # 4. QUERY REWRITING
        rewritten_query = rewrite_query(query)

        print(
            f"\nRewritten query: {rewritten_query}"
        )

        # 5. RETRIEVAL and RERANKING

        context = reranker(
            rewritten_query,
            retriever
        )

        # 6. GENERATION

        prompt = f"""
        You are a research paper question-answering assistant.

        Answer the user's question using ONLY the provided context.

        If the answer cannot be found in the context, say:
        "I don't know based on the provided documents."

        Do not hallucinate or use outside knowledge.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        response = llm.invoke(prompt)

        answer = response.content

        # 7. FINAL ANSWER

        print("\n" + "=" * 60)
        print("ANSWER")
        print("=" * 60)

        print(answer)


if __name__ == "__main__":
    main()