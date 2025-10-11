from crewai import Agent
from .llm_provider import llm

def create_answer_agent():
    return Agent(
        role="Answer Agent",
        goal="Filter out hallucination from the answer.",
        backstory="\n".join([
            "You are a grader assessing whether an answer is useful to resolve a question.",
            "Make sure you meticulously review the answer and check if it makes sense for the question asked",
            "If the answer is relevant generate a clear and concise response.",
            "If the answer gnerated is not relevant then perform a websearch using 'web_search_tool'",
        ]),        
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )  