from crewai import LLM
from helper.config import get_settings

# llm = LLM(
#     model="openrouter/deepseek/deepseek-r1",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=get_settings().OPENROUTER_API_KEY
# )

llm = LLM(
    model="groq/qwen/qwen3-32b",
    api_key = get_settings().GROQ_API_KEY
)

# llm = LLM(
#     model="huggingface/deepseek-ai/DeepSeek-R1",
#     api_key = get_settings().HUGGING_FACE_TOKEN
# )

