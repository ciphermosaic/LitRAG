# Production RAG

A production-oriented Retrieval-Augmented Generation (RAG) pipeline for querying research papers and other document formats.

The project processes documents through ingestion, cleaning, chunking, embedding, vector storage, retrieval, reranking, generation, and evaluation.

## Features

* Multi-format document ingestion
* Document cleaning and preprocessing
* Recursive text chunking
* Semantic embeddings using Sentence Transformers
* ChromaDB vector storage
* Similarity-based document retrieval
* Cross-encoder reranking
* LLM-based answer generation
* RAG evaluation and metrics
* Modular pipeline architecture
* Environment variable support
* Built with Python and `uv`

## RAG Pipeline

```text
Documents
    │
    ▼
┌───────────────┐
│ Document      │
│ Loader        │
└───────┬───────┘
        ▼
┌───────────────┐
│ Cleaning      │
└───────┬───────┘
        ▼
┌───────────────┐
│ Chunking      │
└───────┬───────┘
        ▼
┌───────────────┐
│ Embeddings    │
└───────┬───────┘
        ▼
┌───────────────┐
│ ChromaDB      │
│ Vector Store  │
└───────┬───────┘
        ▼
┌───────────────┐
│ Retriever     │
└───────┬───────┘
        ▼
┌───────────────┐
│ Reranker      │
└───────┬───────┘
        ▼
┌───────────────┐
│ LLM Generator │
└───────┬───────┘
        ▼
      Answer
        │
        ▼
┌───────────────┐
│ Evaluation    │
└───────────────┘
```

## Project Structure

```text
production_rag/
│
├── data/
│   ├── pdfs/
│   │   └── research papers
│   │
│   └── vector_store/
│
├── src/
│   │
│   ├── Ingestion_pipe/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── cleaner.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── pipeline.py
│   │
│   ├── Retrieval_pipe/
│   │   ├── retriever.py
│   │   └── reranker.py
│   │
│   ├── Generation_pipe/
│   │   └── generator.py
│   │
│   ├── Evaluation/
│   │   └── evaluation.py
│   │
│   └── __init__.py
|   |__ main.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── requirements.txt
└── README.md
```

## Technologies

* Python
* LangChain
* ChromaDB
* Sentence Transformers
* Hugging Face Transformers
* PyTorch
* Groq
* `uv`

## Supported Documents

The loader is designed to support multiple document formats.

Currently supported formats include:

* PDF
* TXT
* Markdown
* DOCX
* HTML

Additional formats can be added through the loader configuration without changing the ingestion pipeline.

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/ciphermosaic/LitRAG.git>
cd production_rag
```

### 2. Install dependencies

This project uses `uv`.

```bash
uv sync
```

Alternatively, using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` to GitHub.

## Adding Documents

Place your research papers or supported documents inside:

```text
data/pdfs/
```

For example:

```text
data/pdfs/
├── attention_is_all_you_need.pdf
├── rag_paper.pdf
└── transformer_paper.pdf

upload any data u want.
```

## Running the Ingestion Pipeline

Run:

```bash
uv run python src/Ingestion_pipe/pipeline.py
```

The ingestion pipeline will:

1. Discover supported files.
2. Load the documents.
3. Clean the extracted text.
4. Split documents into chunks.
5. Generate embeddings.
6. Store the chunks and embeddings in ChromaDB.

## Running the RAG System

After ingestion, run:

```bash
uv run python src/main.py
```

The system retrieves relevant chunks, reranks them, passes the relevant context to the generator, and produces an answer based on the retrieved research papers.

## Evaluation

The project includes an evaluation component for measuring RAG performance.

Evaluation can be used to assess:

* Retrieval quality
* Overall RAG performance

## Vector Database

ChromaDB is used as the local vector database.

The vector store contains:

```text
Document chunks
      +
Metadata
      +
Embeddings
```

The local vector database is excluded from Git using `.gitignore`.

## Architecture

The project separates the RAG system into independent components:

```text
Ingestion
    ↓
Retrieval
    ↓
Reranking
    ↓
Generation
    ↓
Evaluation
```

This modular structure makes individual components easier to test, replace, and improve.

## Future Improvements

* Hybrid search using BM25 + dense retrieval
* Query rewriting
* Improved chunking strategies
* Streaming responses
* Automated evaluation pipeline
* Observability
* Production vector database

## License

This project is intended for educational and research purposes.
