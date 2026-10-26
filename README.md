# Enterprise RAG Assistant

An AI-powered knowledge assistant that answers questions about Cognizant using company-related documents. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information and generate context-based answers with a locally running LLM.

## About the Project

The goal of this project is to make it easier to find information from company documents without manually searching through multiple files.

Users can ask questions in natural language, and the application retrieves relevant document chunks from a vector database and uses an LLM to generate an answer.

## Features

- **Document Loading:** Reads company knowledge from Markdown files.
- **Text Chunking:** Splits documents into smaller chunks for efficient retrieval.
- **Embeddings:** Converts text into vector representations using Hugging Face embeddings.
- **Semantic Search:** Retrieves relevant document chunks using Chroma.
- **AI-Powered Answers:** Uses Ollama with the Llama 3.2 model to generate responses.
- **REST API:** Exposes the RAG functionality through FastAPI.
- **Database Integration:** Uses PostgreSQL to store user questions and generated answers.

## Technology Stack

- Python
- FastAPI
- LangChain
- Ollama — Llama 3.2
- Hugging Face Embeddings
- Chroma Vector Database
- PostgreSQL
- SQLAlchemy

## How It Works

1. Company-related Markdown documents are loaded.
2. Documents are split into smaller chunks with overlapping text.
3. Hugging Face embeddings convert the chunks into vectors.
4. Chroma stores the vectors and enables semantic retrieval.
5. A user submits a question through the FastAPI endpoint.
6. The retriever finds relevant document chunks.
7. The retrieved context is added to the system prompt.
8. Ollama generates an answer using the retrieved context.
9. PostgreSQL stores the question and generated answer.
10. The API returns the answer to the user.

## Project Structure

```text
RAG/
├── main.py
├── chat_service.py
├── config.py
├── data_loader.py
├── vector_store.py
├── prompts.py
├── database.py
├── model.py
├── create_table.py
├── .gitignore
└── vector_db/
```

The `vector_db/` directory contains the local Chroma database and is excluded from Git.

## Prerequisites

Before running the application, make sure you have:

- Python installed
- PostgreSQL installed and running
- Ollama installed
- The Llama 3.2 model downloaded
- The required Python packages installed

Download the model with:

```bash
ollama pull llama3.2
```

Start Ollama if it is not already running.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
```

On Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is maintained in the parent project, use its correct path or create one specifically for this project.

### 4. Configure environment variables

Create a `.env` file containing your PostgreSQL connection string:

```env
DATABASE_URL=your_postgresql_connection_string
```

Replace the placeholder with your actual connection string. Do not commit `.env` or expose database credentials on GitHub.

### 5. Create the database table

After configuring PostgreSQL, run:

```bash
python create_table.py
```

### 6. Start the application

From the directory containing `main.py`, run:

```bash
uvicorn main:app --reload
```

The application should be available at:

`http://127.0.0.1:8000`

## API Usage

### Health Check

**Endpoint:** `GET /`

Checks whether the application is accessible.

### Ask a Question

**Endpoint:** `POST /message`

Example request:

```json
{
  "message": "What services does Cognizant provide?"
}
```

The API retrieves relevant information from the knowledge base, generates an answer, stores the question and answer in PostgreSQL, and returns the result.

## Future Improvements

- Add conversation history and session management.
- Support PDF and other document formats.
- Add source citations to generated answers.
- Improve retrieval quality using reranking.
- Add automated tests and structured logging.
- Deploy the application to a cloud environment.

## Learning Outcomes

This project demonstrates practical experience with Retrieval-Augmented Generation, vector databases, embeddings, local LLM integration, REST API development, and relational database integration.

## Disclaimer

This is an independent learning project built using publicly available or appropriately authorized company-related information. It is not an official Cognizant product or an officially endorsed application.
