import os
import uuid
import chromadb


class VectorStoreManager:

    def __init__(
        self,
        persist_directory="data/vector_store",
        collection_name="all_pdfs"
    ):
        self.persist_directory = persist_directory
        self.collection_name = collection_name

        self.client = None
        self.collection = None

        self._initialize_store()

    def _initialize_store(self):

        os.makedirs(
            self.persist_directory,
            exist_ok=True
        )

        self.client = chromadb.PersistentClient(
            path=self.persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={
                "description": "Vector store for RAG documents"
            }
        )

        print(
            f"Initialized collection: {self.collection_name}"
        )

        print(
            f"Documents in collection: {self.collection.count()}"
        )

    def add_documents(self, documents, embeddings):

        if len(documents) != len(embeddings):
            raise ValueError(
                "Number of documents does not match "
                "number of embeddings"
            )

        ids = []
        metadatas = []
        contents = []

        for i, (doc, embedding) in enumerate(
            zip(documents, embeddings)
        ):

            doc_id = f"doc_{uuid.uuid4()}"

            ids.append(doc_id)

            metadata = dict(doc.metadata)

            metadata["index"] = i
            metadata["context_length"] = len(
                doc.page_content
            )

            metadatas.append(metadata)

            contents.append(
                doc.page_content
            )

        self.collection.add(
            ids=ids,
            metadatas=metadatas,
            documents=contents,
            embeddings=embeddings
        )

        print(
            f"Added {len(documents)} documents"
        )

        print(
            f"Documents in collection: "
            f"{self.collection.count()}"
        )

vector_store = VectorStoreManager()