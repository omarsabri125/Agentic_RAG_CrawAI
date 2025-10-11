from crewai import Crew, Process
from agents import (create_router_agent, create_retriever_agent, create_grader_agent,
                    create_hallucination_agent, create_answer_agent)
from tasks import (create_router_task, create_retriever_task, create_grade_task,
                   create_hallucination_task, create_answer_task)
from tools import create_pdf_tool, create_tavily_search


def main(question: str):

    # Create tools
    file_path = "assets/Transformer_paper.pdf"
    pdf_tool = create_pdf_tool(pdf_file = file_path)

    # Create agents
    router_agent = create_router_agent()
    retriever_agent = create_retriever_agent()
    grade_agent = create_grader_agent()
    hallucination_agent = create_hallucination_agent()
    answer_agent = create_answer_agent()

    # Create tasks
    router_task = create_router_task(router_agent)
    retriever_task = create_retriever_task(
        retriever_agent, router_task, pdf_tool, create_tavily_search)
    grade_task = create_grade_task(grade_agent, retriever_task)
    hallucination_task = create_hallucination_task(
        hallucination_agent, grade_task)
    answer_task = create_answer_task(
        answer_agent, hallucination_task, create_tavily_search)

    # Create crew
    crew = Crew(
        agents=[router_agent, retriever_agent, grade_agent,
                hallucination_agent, answer_agent],
        tasks=[router_task, retriever_task, grade_task,
               hallucination_task, answer_task],
        process=Process.sequential,
    )

    result = crew.kickoff(inputs={"question": question})

    return result


# test_question = "what is the self-attention in transformers?"
# Who won the Nobel Prize in Physics 2025?
# What are the latest advancements in AI released by OpenAI this month?
# "When was the latest iPhone model released?"
if __name__ == "__main__":
    test_question = "What are the latest advancements in AI released by OpenAI this month?"
    result = main(question=test_question)
    print(result)
