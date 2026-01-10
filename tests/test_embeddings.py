from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
import numpy as np

# Load + chunk PDF
docs = load_pdf("data/sample.pdf")
chunks = chunk_documents(docs)

texts = [doc.page_content for doc in chunks]

# Embed
embedder = EmbeddingModel()
embeddings = embedder.embed_texts(texts)

# Vector store
vector_store = FAISSVectorStore(embedding_dim=len(embeddings[0]))
vector_store.add(np.array(embeddings), chunks)

# Query
query = "What is this document about?"
query_embedding = embedder.embed_texts([query])

results = vector_store.search(query_embedding, k=3)

print("\nTop retrieved chunks:\n")
for i, doc in enumerate(results, 1):
    print(f"{i}. Source: {doc.metadata}")
    print(doc.page_content[:300])
    print("-" * 40)
