from app.embeddings.embedder import EmbeddingModel
from app.embeddings.vector_store import FAISSVectorStore
from app.rag.prompt import RAG_PROMPT_TEMPLATE
from app.rag.llm import LLMClient


class RAGPipeline:
    def __init__(self, vector_store: FAISSVectorStore):
        self.embedder = EmbeddingModel()
        self.vector_store = vector_store
        self.llm = LLMClient(use_mock=True)

    def answer(self, question: str, k: int = 5) -> dict:
        # Embed query
        query_embedding = self.embedder.embed_texts([question])

        # Retrieve docs
        docs = self.vector_store.search(query_embedding, k=k)

        # Build context
        context_blocks = []
        sources = []

        for doc in docs:
            context_blocks.append(doc.page_content)
            sources.append(doc.metadata)

        context = "\n\n".join(context_blocks)

        # Prompt
        prompt = RAG_PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )

        # Generate answer
        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": sources
        }
