from crewai import Task
from pydantic import BaseModel, Field

class RouteDecision(BaseModel):
    route: str = Field(
        ...,
        description= "\n".join([ 
            "Routing decision — must be either 'vectorstore' or 'web_search'. ",
            "'vectorstore' if the question can be answered from the internal knowledge base, ",
            "'web_search' otherwise.",
        ]),
        pattern="^(vectorstore|web_search)$" 
    )

def create_router_task(router_agent):
    return Task(
        description="\n".join([
            "Analyze the given question {question} to determine the appropriate search method:",
            "1. Use 'vectorstore' if:",
            "   - The question contains a keyword or a similar words",
            "   - The topic is likely covered in our vector database",
            "2. Use 'web_search' if:",
            "   - The topic requires current or real-time information",
            "   - The question is about general topics not covered in our vector database",
            "Make decisions based on semantic understanding rather than keyword matching."
        ]),
        expected_output= "A valid JSON following the RouteDecision schema (with a single field: 'route').",
        output_json= RouteDecision,
        agent= router_agent
    )
