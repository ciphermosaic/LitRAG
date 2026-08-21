from langchain_text_splitters import (RecursiveCharacterTextSplitter, 
                                      MarkdownTextSplitter,
                                      CharacterTextSplitter,
                                      TokenTextSplitter,
                                      Language
)

from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()


# SAMPLE_TEXT = """..."""
# SAMPLE_CODE = """..."""

def recursive_splitter(documents):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
    )

    chunks  = text_splitter.split_documents(documents)

    return chunks

def MKSplitter(documents):
    headers_to_consider = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3")
    ]

    splitter = MarkdownTextSplitter(headers_to_split_on=headers_to_consider)
    chunks = splitter.split_text(documents)

    print(f"Markdown Splitter produces {len(chunks)} chunks.")

    return chunks

def code_splitter(code):
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=500, chunk_overlap=50
    )

    chunks = python_splitter.split_text(code)
    print(f"Code Splitter produces {len(chunks)} chunks.")

    return chunks

def document_splitter(docs, folder_path):
    from langchain_community.document_loaders import PyMuPDFLoader

    loader = PyMuPDFLoader(folder_path)
    doc = loader.load()

    print(f"Loader {len(docs)} docs from PDF.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    print(f"splitted into {len(chunks)} chunks.")
    print(f"First chunk metadata {chunks[0].metadata}")
    print(f"First chunk page content {chunks[0].page_content[:200]}...")


if __name__ == "__main__":
    print("===Document splitter from pdf===")
    document_splitter()
