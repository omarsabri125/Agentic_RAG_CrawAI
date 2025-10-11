from crewai import Agent
from .llm_provider import llm

def create_hallucination_agent():
    return Agent(
        role="Hallucination Grader",
        goal="Filter out hallucination",
        backstory=(
            "You are a hallucination grader assessing whether an answer is grounded in / supported by a set of facts."
            "Make sure you meticulously review the answer and check if the response provided is in alignmnet with the question asked"
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
