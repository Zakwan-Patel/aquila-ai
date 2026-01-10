🦅 Aquila AI

Enterprise-Grade Multi-Agent RAG System

Aquila is a production-style AI Knowledge & Decision Assistant built using Retrieval-Augmented Generation (RAG) and multi-agent orchestration.
It enables grounded, verifiable answers from unstructured documents using modern LLM pipelines.

🚀 Key Features

📄 Document Ingestion – PDF loading, cleaning, chunking with metadata

🧠 Semantic Memory – FAISS vector store with sentence embeddings

🔍 Grounded RAG – Answers generated strictly from retrieved context

🤖 Multi-Agent Architecture – Retriever, Analyst, Verifier agents via LangGraph

🛡️ Hallucination Control – Verification layer enforces evidence-based responses

🌐 API-First Design – FastAPI backend with clean schemas

🎨 User Interface – Streamlit chat UI for non-technical users

🐳 Fully Containerized – Docker & Docker Compose support

🏗️ System Architecture
User
 ↓
Streamlit UI
 ↓
FastAPI Backend
 ↓
LangGraph Agent Orchestrator
 ├── Retriever Agent (FAISS)
 ├── Analyst Agent (LLM)
 └── Verifier Agent (Grounding Check)
 ↓
Final Answer + Sources

🛠️ Tech Stack

Backend

Python 3.10

FastAPI

LangChain, LangGraph

FAISS

Sentence-Transformers

OpenAI (pluggable, mock supported)

Frontend

Streamlit

Infrastructure

Docker

Docker Compose

⚙️ Getting Started (Docker)
Prerequisites

Docker & Docker Compose installed

Run the System
docker compose up --build

Access

UI: http://localhost:8501

API Docs: http://localhost:8000/docs

🧪 Example Query

“What is the main topic of this document?”

Response:

Grounded answer

Source document + page references

Verification status

🔒 Design Principles

Evidence before reasoning

Deterministic agent flows

Separation of concerns

Production-first architecture

📌 Future Enhancements

SQL Agent for structured data

Role-based access control

Local LLM support (LLaMA / Mistral)

Cloud deployment (AWS / Azure)

📜 License

MIT

🙏 Note

Built with a focus on clarity, correctness, and real-world engineering practices.