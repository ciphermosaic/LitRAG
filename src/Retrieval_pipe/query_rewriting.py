import os
from dotenv import load_dotenv
from Evaluation.llm import llm
from langchain_groq import ChatGroq

load_dotenv()


def rewrite_query(user_query, chat_history):
    prompt = f"""Rewrite the user query to be specific search query.
    Resolve pronouns/References using chat history.
    user query query : {user_query}

    Return only the rewritten query.
    """

    response = llm.invoke(prompt).content.strip()
    return response