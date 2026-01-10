import faiss
import numpy as np
from typing import List
from langchain_core.documents import Document


class FAISSVectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents: List[Document] = []

    def add(self, embeddings: np.ndarray, documents: List[Document]):
        self.index.add(embeddings)
        self.documents.extend(documents)

    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Document]:
        distances, indices = self.index.search(query_embedding, k)
        return [self.documents[i] for i in indices[0]]
