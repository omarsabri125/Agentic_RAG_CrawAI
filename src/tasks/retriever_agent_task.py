from crewai import Task
from pydantic import BaseModel, Field

class RetrievedAnswer(BaseModel):
    context: str = Field(
        ...,
        description="\n".join([
            "You should analyse the output of the 'router_task'",
            "If the response is 'websearch' then use the web_search_tool to retrieve information from the web.",
            "If the response is 'vectorstore' then use the rag_tool to retrieve information from the vectorstore.",
            "Return a claer and consise text as response."
        ])
    )

def create_retriever_task(retriever_agent, router_task, pdf_tool, create_tavily_search):
    return Task(
        description= "\n".join([
            "Based on the response from the router task extract information for the question {question} with the help of the respective tool.",
            "Use the web_serach_tool to retrieve information from the web in case the router task output is 'web_search'. You should pass the input query {question} to the web_search_tool.", 
            "Use the rag_tool to retrieve information from the vectorstore in case the router task output is 'vectorstore'."
        ]),
        expected_output= "\n".join([
            "A valid JSON following the RetrievedAnswer schema (with a single field: 'context').",
            "Return only clear, factual, and concise text related to the question.",
            "No preambles, explanations, or formatting — only the relevant retrieved content."
        ]),
        output_json= RetrievedAnswer,
        agent= retriever_agent,
        context= [router_task],
        tools= [pdf_tool, create_tavily_search]
    )

