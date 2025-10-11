from crewai import Task
from pydantic import BaseModel, Field

class GradeDecision(BaseModel):
    relevance: str = Field(
        ...,
        description= "\n".join([
            "Binary decision indicating if the retrieved content is relevant to the question.",
            "Must be exactly 'yes' if the retriever's output aligns with the question,",
            "and exactly 'no' if it does not. Respond strictly with 'yes' or 'no'.",
        ]),
        pattern="^(yes|no)$"
    )

def create_grade_task(grade_agent, retriever_task):
    return Task(
        description= "\n".join([
            "Evaluate whether the content retrieved by the retriever task for the question {question} ",
            "is semantically relevant to the user's query. Base your decision on meaning, not keywords.",
        ]),
        expected_output= "\n".join([
            "A valid JSON following the GradeDecision schema",
            "(with a single field: 'relevance').",
            "You must respond strictly with either 'yes' or 'no' — ",
            "no other words are allowed.",
            ]),
        output_json= GradeDecision,
        agent= grade_agent,
        context=[retriever_task],
    )