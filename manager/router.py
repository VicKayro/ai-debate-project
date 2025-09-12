# manager/router.py
from typing import List, Dict, Tuple
from agents import superceo, supercto, superproduct
from agents.synthetizer import synthesize
import re

SpeakerFn = Tuple[str, callable]

def _trim_to_n_sentences(text: str, n: int = 2) -> str:
    parts = re.split(r'(?<=[\.\!\?])\s+', text.strip())
    return " ".join(parts[:n]).strip()

def run_debate(question: str, rounds: int = 2, order: List[SpeakerFn] = None) -> tuple[list[dict], str]:
    """
    Lance un débat court où chaque agent réagit au DERNIER message.
    - Mémoire courte: on ne fournit aux agents que les 2 derniers messages.
    - Tours courts: 2 phrases max (post-troncature en sécurité).
    """
    if order is None:
        order = [("CEO", superceo.respond), ("CTO", supercto.respond), ("PM", superproduct.respond)]

    thread: List[Dict[str, str]] = []

    # Premier tour: le premier agent réagit à la QUESTION (pas de contexte)
    first_name, first_fn = order[0]
    first_msg = first_fn(question, thread)
    thread.append({"speaker": first_name, "text": _trim_to_n_sentences(first_msg)})

    # Boucle de tours: chacun réagit au DERNIER message
    for _ in range(rounds):
        for name, fn in order[1:] + [order[0]]:  # fait tourner l'initiative
            reply = fn(question, thread)
            thread.append({"speaker": name, "text": _trim_to_n_sentences(reply)})

    # Synthèse finale courte
    recap = synthesize(question, thread)
    return thread, recap
