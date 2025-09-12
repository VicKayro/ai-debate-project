from utils.llm import chat

def synthesize(question: str, thread: list[dict]) -> str:
    convo = "\n".join([f"{m['speaker']}: {m['text']}" for m in thread])
    prompt = f"""
Tu es facilitateur. Fais une synthèse **très concise** du débat sur: "{question}"

Donne:
- 2 points d'accord max
- 2 points de désaccord max
- 3 actions concrètes (qui/quoi/quand si possible)

Débat:
{convo}

Réponse en 6 lignes max, puces courtes.
"""
    return chat(prompt, temperature=0.2, max_tokens=220)
