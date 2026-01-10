from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
from app.agents.state import AgentState


class RetrieverAgent:
    def __init__(self, vector_store: FAISSVectorStore, k: int = 5):
        self.vector_store = vector_store
        self.embedder = EmbeddingModel()
        self.k = k

    def run(self, state: AgentState) -> AgentState:
        query_embedding = self.embedder.embed_texts([state["question"]])
        docs = self.vector_store.search(query_embedding, k=self.k)

        state["documents"] = docs
        return state
