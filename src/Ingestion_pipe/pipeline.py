# ingestion.py
from Ingestion_pipe.loader import load_document, loaders
from Ingestion_pipe.cleaner import clean_documents
from Ingestion_pipe.chunking import document_splitter
from Ingestion_pipe.embeddings import create_embeddings
from Ingestion_pipe.vector_store import VectorStoreManager

def ingest(file_path):
    # 1. Load documents
    documents = load_document(file_path)

    # 2. Clean documents
    documents = clean_documents(documents)
    # 3. Split into chunks
    chunks = document_splitter(documents)

    # 4. Create embeddings
    embeddings = create_embeddings(chunks)

    # 5. Store in vector database
    vector_store = VectorStoreManager()
    vector_store.add_documents(chunks, embeddings)

    return vector_store


from pathlib import Path

if __name__ == "__main__":
    folder = Path("data/pdfs")

    for file_path in folder.iterdir():

        if file_path.is_file():
            ext = file_path.suffix.lower()

            if ext in loaders:
                print(f"Ingesting: {file_path}")
                ingest(str(file_path))
            else:
                print(f"Skipping unsupported file: {file_path.name}")

    print("Ingestion completed successfully!")
