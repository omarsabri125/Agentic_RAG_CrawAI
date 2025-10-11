from crewai import Agent
from .llm_provider import llm

def create_retriever_agent():
    return Agent(
        role= "Retriever Agent",
        goal= "Answer the user's question using the appropriate source based on the router's decision.",
        backstory= "\n".join([
            "You are an intelligent retriever who answers user questions using the correct information source. ",
            "If the router decides 'vectorstore', use the RAG tool to find the answer. ",
            "If the router decides 'web_search', use the web search tool to get up-to-date information. ",
            "Your goal is to return a clear, concise, and factual answer."
        ]),
        verbose= True,
        allow_delegation= False,
        llm=llm,
    )
