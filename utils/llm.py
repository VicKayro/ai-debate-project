import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Charger .env si présent (local)
load_dotenv()

def get_api_key():
    # 1. Si on est dans Streamlit Cloud
    try:
        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass  # pas de secrets quand on n'est pas dans Streamlit

    # 2. Sinon, fallback sur .env
    return os.getenv("OPENAI_API_KEY")

_client = OpenAI(api_key=get_api_key())

def chat(prompt: str, model: str = "gpt-4o-mini", temperature: float = 0.7, max_tokens: int = 160) -> str:
    resp = _client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content.strip()
