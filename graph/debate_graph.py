from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.superproduct import get_superproduct_agent
from agents.supercto import get_supercto_agent
from agents.superceo import get_superceo_agent
from agents.synthesizer import get_synthesizer_agent


# 🧠 Etat partagé du graph (conversation)
class DebateState(TypedDict):
    history: list[str]
    round: int
    max_rounds: int

# 🧩 Agents
superproduct = get_superproduct_agent()
supercto = get_supercto_agent()
superceo = get_superceo_agent()
synthesizer = get_synthesizer_agent()


agents_cycle = [("SuperProduct", superproduct), ("SuperCTO", supercto), ("SuperCEO", superceo)]

def debate_node(state: DebateState):
    current_agent_index = state["round"] % len(agents_cycle)
    name, agent = agents_cycle[current_agent_index]
    input_message = "\n".join(state["history"][-1:])  # prend dernier message
    response = agent.invoke({"input": input_message})
    state["history"].append(f"{name}: {response.content}")
    state["round"] += 1
    return state

def check_continue(state: DebateState):
    return "continue" if state["round"] < state["max_rounds"] else "end"

def build_debate_graph():
    builder = StateGraph(DebateState)
    builder.add_node("debate_step", debate_node)
    builder.add_node("synthesis", synthesize_summary)
    builder.set_entry_point("debate_step")
    builder.add_conditional_edges("debate_step", check_continue, {
        "continue": "debate_step",
        "end": "synthesis"
    })
    builder.add_edge("synthesis", END)
    return builder.compile()


def synthesize_summary(state: DebateState):
    debate_text = "\n".join(state["history"])
    response = synthesizer.invoke({"input": debate_text})
    state["history"].append("🧠 Synthèse finale :\n" + response.content)
    return state
