from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
from app.rag.rag_pipeline import RAGPipeline
import numpy as np

# Prepare documents
docs = load_pdf("data/sample.pdf")
chunks = chunk_documents(docs)

texts = [doc.page_content for doc in chunks]

embedder = EmbeddingModel()
embeddings = embedder.embed_texts(texts)

vector_store = FAISSVectorStore(embedding_dim=len(embeddings[0]))
vector_store.add(np.array(embeddings), chunks)

# RAG
rag = RAGPipeline(vector_store)

question = "What is the main topic of this document?"
result = rag.answer(question)

print("\nANSWER:\n")
print(result["answer"])

print("\nSOURCES:\n")
for src in result["sources"]:
    print(src)
