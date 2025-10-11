from crewai_tools import PDFSearchTool
from crewai.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from helper.config import Settings, get_settings

def create_pdf_tool(pdf_file: str):

    tool = PDFSearchTool(pdf=pdf_file,
                         config=dict(
                             llm=dict(
                                 provider="groq",
                                 config=dict(
                                     model="llama-3.3-70b-versatile",
                                     api_token=get_settings().GROQ_API_KEY
                                     # temperature=0.5,
                                     # top_p=1,
                                 ),
                             ),
                             embedder=dict(
                                 provider="huggingface",
                                 config=dict(
                                     model="BAAI/bge-small-en-v1.5",
                                     api_token=get_settings().HUGGING_FACE_TOKEN
                                     # task_type="retrieval_document",
                                 ),
                             ),
                         )

                         )

    return tool


@tool("tavily_search")
def create_tavily_search(query: str) -> str:
    """This tool searches for relevant results using TavilySearchResults and returns the top-k results for a given query."""

    tool_instance = TavilySearchResults(k=3, tavily_api_key = get_settings().TAVILY_API_KEY)

    return tool_instance.run(query)

