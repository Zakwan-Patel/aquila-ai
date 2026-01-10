from app.rag.prompt import RAG_PROMPT_TEMPLATE
from app.rag.llm import LLMClient
from app.agents.state import AgentState


class AnalystAgent:
    def __init__(self):
        self.llm = LLMClient(use_mock=True)

    def run(self, state: AgentState) -> AgentState:
        context = "\n\n".join(doc.page_content for doc in state["documents"])

        prompt = RAG_PROMPT_TEMPLATE.format(
            context=context,
            question=state["question"]
        )

        state["answer"] = self.llm.generate(prompt)
        return state
