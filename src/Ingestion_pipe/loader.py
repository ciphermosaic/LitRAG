from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_unstructured import UnstructuredLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader


def load_document(file_path: str):
    path = Path(file_path)
    ext = path.suffix.lower()

    loaders = {
        ".pdf": PyMuPDFLoader,
        ".txt": TextLoader,
        ".md": UnstructuredMarkdownLoader,
        ".docx": UnstructuredLoader,
    }

    if ext not in loaders:
        raise ValueError(f"Unsupported file type: {ext}")

    loader = loaders[ext](str(path))
    documents = loader.load()

    for doc in documents:
        doc.metadata["source"] = str(path)
        doc.metadata["file_name"] = path.name

    return documents