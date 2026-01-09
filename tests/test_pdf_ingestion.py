from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_documents

docs = load_pdf("data/sample.pdf")
chunks = chunk_documents(docs)

print(f"Pages loaded: {len(docs)}")
print(f"Chunks created: {len(chunks)}")

print("\nSample chunk:\n")
print(chunks[0].page_content[:500])
print("\nMetadata:", chunks[0].metadata)
