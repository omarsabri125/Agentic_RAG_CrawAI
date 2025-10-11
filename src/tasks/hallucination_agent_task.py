from crewai import Task
from pydantic import BaseModel, Field


class HallucinationDecision(BaseModel):
    grounded: str = Field(
        ...,
        description="\n".join([
            "Binary decision indicating if the answer is grounded in factual information.",
            "Must be exactly 'yes' if the answer is supported by facts or 'no' if it is not.",
            "Respond strictly with 'yes' or 'no'. No other values are allowed.",
            # "Binary score 'yes' or 'no' score to indicate whether the answer is sync with the question asked",
            # "Respond 'yes' if the answer is in useful and contains fact about the question asked.",
            # "Respond 'no' if the answer is not useful and does not contains fact about the question asked.",
            # "Do not provide any preamble or explanations except for 'yes' or 'no'.",
        ]),
        pattern="^(yes|no)$"
    )


def create_hallucination_task(hallucination_grader, grader_task):
    return Task(
        description=(
            "Based on the response from the grader task for the quetion {question} evaluate whether the answer is grounded in / supported by a set of facts."
        ),
        expected_output="\n".join([
            "A valid JSON following the HallucinationDecision schema (with a single field: 'grounded').",
            "You must respond strictly with either 'yes' or 'no' — ",
            "no other words are allowed.",
        ]),
        output_json=HallucinationDecision,
        agent=hallucination_grader,
        context=[grader_task],
    )
