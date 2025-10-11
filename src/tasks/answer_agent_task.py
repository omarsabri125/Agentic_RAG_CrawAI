from crewai import Task
from pydantic import BaseModel, Field

class FinalAnswer(BaseModel):
    answer: str = Field(
        ...,
        description="\n".join([
            "The final answer to the input question.",
            "Return a clear and concise response only.",
            "Do not include preamble, explanations, or extra text.",
            "If the hallucination_task output is 'no', perform a web search and return the concise answer.",
            "If unable to find a valid response, return: 'Sorry! unable to find a valid response'."
        ])
    )


def create_answer_task(answer_agent, hallucination_task, create_tavily_search):
    return Task(
        description= "\n".join([
            "Based on the response from the hallucination task for the quetion {question} evaluate whether the answer is useful to resolve the question.",
            "If the answer is 'yes' return a clear and concise answer.",
            "If the answer is 'no' then perform a 'websearch' and return the response",
        ]),
        expected_output= "A valid JSON following the FinalAnswer schema (with a single field: 'answer').",
        # "\n".join([
        #     "Return a clear and concise response if the response from 'hallucination_task' is 'yes'.",
        #     "Perform a web search using 'web_search_tool' and return ta clear and concise response only if the response from 'hallucination_task' is 'no'.",
        #     "Otherwise respond as 'Sorry! unable to find a valid response'.",
        #     "Make sure the final response is clear and concise and contain only the answer to the input question without any preamble or explanation as this answer will be presnted to the user.",
        #     "The final answer should be a clear and concise response to the input question.",
        # ]),
        output_json= FinalAnswer,
        agent= answer_agent,
        context= [hallucination_task],
        tools= [create_tavily_search],
    )

# from crewai import Task
# from pydantic import BaseModel, Field

# class FinalAnswer(BaseModel):
#     answer: str = Field(
#         ...,
#         description="\n".join([
#             "The final answer to the input question.",
#             "Return a clear and concise response only.",
#             "Do not include preamble, explanations, or extra text.",
#             "If the hallucination_task output is 'no', you MUST perform a web search using the provided tool 'create_tavily_search' with the input question as query.",
#             "Use the search results to generate a clear and factual answer.",
#             "If unable to find a valid response, return: 'Sorry! unable to find a valid response'."
#         ])
#     )


# def create_answer_task(answer_agent, hallucination_task, create_tavily_search):
#     return Task(
#         description="\n".join([
#             "You are the final decision-making agent.",
#             "You receive the output from the hallucination task for the question: {question}.",
#             "If the hallucination_task output ('grounded') is 'yes', return a clear and concise answer directly.",
#             "If the hallucination_task output ('grounded') is 'no', you MUST perform a web search using the tool 'create_tavily_search'.",
#             "Use the search results to answer the question concisely and accurately.",
#             "If nothing relevant is found, return 'Sorry! unable to find a valid response'.",
#         ]),
#         expected_output="A valid JSON following the FinalAnswer schema (with a single field: 'answer').",
#         output_json=FinalAnswer,
#         agent=answer_agent,
#         context=[hallucination_task],
#         tools=[create_tavily_search],
#     )
