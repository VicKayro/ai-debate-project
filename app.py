import os
import streamlit as st
from dotenv import load_dotenv
from graph.debate_graph import build_debate_graph
from utils.pdf_reader import extract_text_from_pdf


# Charger variables d'environnement
load_dotenv()

st.set_page_config(page_title="Débat multi-agents", layout="wide")

st.title("🎭 Débat Multi-Agents : SuperCEO, SuperCTO & SuperProduct")

with st.form("question_form"):
    question = st.text_area("🧠 Pose une question complexe :", height=150, placeholder="Ex : Quelle stratégie pour lancer une app B2B ?")
    max_rounds = st.slider("Nombre de tours de débat :", min_value=1, max_value=12, value=6, step=1)
    submitted = st.form_submit_button("🚀 Lancer le débat")
    uploaded_file = st.file_uploader("📄 Uploader un PDF en contexte (optionnel)", type=["pdf"])


if submitted and question:
    st.info("Débat en cours... cela peut prendre quelques secondes ⏳")

    # Construire le graphe
    graph = build_debate_graph()

    # Initialiser l'état
    state = {
        "history": [f"USER: {question}"],
        "round": 0,
        "max_rounds": max_rounds
    }

    # Lancer le débat
    result = graph.invoke(state)

    st.success("✅ Débat terminé !")

    # Afficher l’historique
    st.subheader("🗣️ Historique du débat")
    for msg in result["history"]:
        speaker, content = msg.split(":", 1)
        st.markdown(f"**{speaker.strip()}** : {content.strip()}")

    # Afficher la synthèse
    st.subheader("🧠 Synthèse finale")
    st.markdown(result["summary"])

    context = ""
if uploaded_file is not None:
    context = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF chargé avec succès")

# Lancer le débat
graph = build_debate_graph()

# Injecter le contexte dans le prompt initial
initial_input = f"{question}\n\n---\n📄 CONTEXTE FOURNI :\n{context}" if context else question

state = {
    "history": [f"USER: {initial_input}"],
    "round": 0,
    "max_rounds": max_rounds
}

result = graph.invoke(state)



