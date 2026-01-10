from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
from app.agents.graph import build_agent_graph
import numpy as np

# Prepare documents
docs = load_pdf("data/sample.pdf")
chunks = chunk_documents(docs)

texts = [doc.page_content for doc in chunks]

embedder = EmbeddingModel()
embeddings = embedder.embed_texts(texts)

vector_store = FAISSVectorStore(embedding_dim=len(embeddings[0]))
vector_store.add(np.array(embeddings), chunks)

# Build agent graph
graph = build_agent_graph(vector_store)

# Run
result = graph.invoke({
    "question": "What is the main topic of this document?",
    "documents": [],
    "answer": "",
    "verified": False
})

print("\nFINAL ANSWER:\n")
print(result["answer"])

print("\nVERIFIED:", result["verified"])
