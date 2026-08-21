import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

def get_llm():
    llm = ChatGroq(
        model_name="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=500,
        groq_api_key = "GROQ_API_KEY"
    )

    return llm

llm = get_llm()