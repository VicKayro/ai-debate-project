from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

def get_synthesizer_agent():
    system_prompt = """Tu es un expert en communication stratégique. Ta mission est de lire un débat multi-agent, et de générer :
- un résumé clair et structuré des idées clés de chaque agent
- les contradictions ou divergences de points de vue
- une recommandation finale, en tenant compte de toutes les perspectives

Réponds en français, en étant clair, synthétique et percutant."""

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template("{input}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    return prompt | llm
