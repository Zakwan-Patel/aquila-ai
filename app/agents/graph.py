from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.retriever import RetrieverAgent
from app.agents.analyst import AnalystAgent
from app.agents.verifier import VerifierAgent


def build_agent_graph(vector_store):
    retriever = RetrieverAgent(vector_store)
    analyst = AnalystAgent()
    verifier = VerifierAgent()

    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retriever.run)
    graph.add_node("analyze", analyst.run)
    graph.add_node("verify", verifier.run)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "analyze")
    graph.add_edge("analyze", "verify")
    graph.add_edge("verify", END)

    return graph.compile()
