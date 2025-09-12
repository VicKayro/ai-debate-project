# AI Team Debate

Trois agents IA (SuperCEO, SuperCTO et SuperProduct) débattent de tes questions techs.  
Parce qu’un seul avis, c’est surfait.  

Démo : [ai-team-debate2.streamlit.app](https://ai-team-debate2.streamlit.app/)

---

## Pourquoi ?
- Tu poses une question compliquée (ex: *"Faut-il lancer une marketplace B2B en 2025 ?"*)  
- Trois IA avec des égos démesurés se répondent (ou s’ignorent, comme dans un vrai comité de direction).  
- À la fin, un synthétiseur fait le tri et te balance un résumé intelligent.  
- Bref : un board meeting, mais sans ppt.

---

## Installation locale

Clone le repo :

```bash
git clone https://github.com/VicKayro/ai-debate-project.git
cd ai-debate-project
````

Crée un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installe les dépendances :

```bash
pip install -r requirements.txt
```

Ajoute ta clé OpenAI dans un fichier `.env` :

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

Lance l’app :

```bash
streamlit run app.py
```

---

## ☁️ Déploiement Streamlit Cloud

1. Fork ce repo (ou pousse ton fork).
2. Va sur [Streamlit Cloud](https://share.streamlit.io/), clique *New App*.
3. Donne-lui ton repo + `app.py`.
4. Ajoute tes secrets dans **Settings > Secrets** :

```toml
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

5. Clique *Deploy*.
6. Apprécie ton nouveau joujou en ligne.

---

## Tech stack

* [Streamlit](https://streamlit.io/) 
* [OpenAI GPT-4o-mini](https://platform.openai.com/) 
* [PyMuPDF](https://pymupdf.readthedocs.io/)
* Python 3.11 

---


## ⭐Contribuer

Un PR ? Un bugfix ? Une nouvelle IA genre *SuperIntern* qui pose trop de questions ?
Fork, PR, et on merge :)

