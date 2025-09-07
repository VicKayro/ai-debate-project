import os
from dotenv import load_dotenv
from graph.debate_graph import build_debate_graph

load_dotenv()

graph = build_debate_graph()

initial_question = "Voilà mon idée de projet : [un agent autonome qui gère les factures dans les mairies et les affecte aux chefs de services], aidez moi à le concevoir au mieux"

state = {
    "history": [f"USER: {initial_question}"],
    "round": 0,
    "max_rounds": 6
}

final_state = graph.invoke(state)

print("\n\n🎤 Résultat du débat :\n")
for line in final_state["history"]:
    print(line)
