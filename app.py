import os
import streamlit as st
from dotenv import load_dotenv
from manager.router import run_debate
from utils.pdf_reader import extract_text_from_pdf

# Charger variables d'environnement
load_dotenv()

st.set_page_config(page_title="Débat multi-agents", layout="wide")

st.title("Débat Multi-Agents : SuperCEO, SuperCTO & SuperProduct")

with st.form("question_form"):
    question = st.text_area(
        "🧠 Pose une question complexe :",
        height=150,
        placeholder="Ex : Quelle stratégie pour lancer une app B2B ?"
    )
    max_rounds = st.slider(
        "Nombre de tours de débat :",
        min_value=1, max_value=12, value=6, step=1
    )
    submitted = st.form_submit_button("🚀 Lancer le débat")
    uploaded_file = st.file_uploader(
        "📄 Uploader un PDF en contexte (optionnel)", type=["pdf"]
    )

# Extraire texte PDF si fourni
context = ""
if uploaded_file is not None:
    context = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF chargé avec succès")

# Quand l’utilisateur lance le débat
if submitted and question:
    st.info("Débat en cours... cela peut prendre quelques secondes ⏳")

    # Construire la question avec contexte si dispo
    initial_input = f"{question}\n\n---\n📄 CONTEXTE FOURNI :\n{context}" if context else question

    # 👉 Nouvelle logique : run_debate
    thread, recap = run_debate(question=initial_input, rounds=max_rounds)

    st.success("✅ Débat terminé !")

    # Transcript du débat
    st.subheader("🗣️ Historique du débat")
    for m in thread:
        st.markdown(f"**{m['speaker']}** : {m['text']}")

    # Synthèse finale
    st.subheader("Synthèse finale")
    st.markdown(recap)
