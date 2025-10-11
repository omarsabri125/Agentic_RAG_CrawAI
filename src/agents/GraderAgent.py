from crewai import Agent
from .llm_provider import llm

def create_grader_agent():
    return Agent(
        role= "Answer Grader Agent",
        goal = "Filter out erroneous retrievals",
        backstory= "\n".join([
            "You are a grader assessing relevance of a retrieved document to a user question.",
            "If the document contains keywords related to the user question, grade it as relevant.",
            "It does not need to be a stringent test.You have to make sure that the answer is relevant to the question."
        ]),
        verbose= True,
        allow_delegation= False,
        llm= llm
    )
