from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.graph import build_agent_graph
from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_documents
import numpy as np

# ✅ DEFINE ROUTER FIRST
router = APIRouter(prefix="/rag", tags=["RAG"])


# ---------- Bootstrap (runs once on startup) ----------
docs = load_pdf("data/sample.pdf")
chunks = chunk_documents(docs)

texts = [doc.page_content for doc in chunks]
embedder = EmbeddingModel()
embeddings = embedder.embed_texts(texts)

vector_store = FAISSVectorStore(embedding_dim=len(embeddings[0]))
vector_store.add(np.array(embeddings), chunks)

graph = build_agent_graph(vector_store)
# ----------------------------------------------------


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):
    result = graph.invoke({
        "question": request.question,
        "documents": [],
        "answer": "",
        "verified": False
    })

    sources = []
    for doc in result.get("documents", []):
        meta = doc.metadata or {}
        preview = doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content

        sources.append({
            "source": meta.get("source", "unknown"),
            "page": meta.get("page", "unknown"),
            "preview": preview
        })

    return {
        "answer": result["answer"],
        "verified": result["verified"],
        "sources": sources
    }
