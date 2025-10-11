from crewai import Agent
from .llm_provider import llm

def create_router_agent():
    return Agent(
        role= "Router Agent",
        goal='Route user questions to either vectorstore or web search based on content relevance',
        backstory="\n".join([
            "You are an expert at determining whether a question can be answered using the ",
            "information stored in our vector database, or requires a web search. ",
            "You understand that the vector database contains comprehensive knowledge base ",
            "You make routing decisions based on the semantic meaning of questions rather than just keyword matching."
        ]),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

