from app.agents.state import AgentState


class VerifierAgent:
    def run(self, state: AgentState) -> AgentState:
        answer = state.get("answer", "").lower()

        if "i do not know" in answer or len(state["documents"]) > 0:
            state["verified"] = True
        else:
            state["verified"] = False
            state["answer"] = (
                "I cannot verify this answer using the provided documents."
            )

        return state
