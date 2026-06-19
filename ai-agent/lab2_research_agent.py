# import os
# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
# from langchain_community.utilities import WikipediaAPIWrapper

# # Load env
# load_dotenv()

# # API key
# api_key = os.getenv("OPENAI_API_KEY")

# # LLM (OpenRouter)
# llm = ChatOpenAI(
#     openai_api_key=api_key,
#     openai_api_base="https://openrouter.ai/api/v1",
#     model="meta-llama/llama-3-8b-instruct",
#     temperature=0
# )

# # Tools
# search = DuckDuckGoSearchRun()
# wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# tools = [search, wiki]

# # ✅ Bind tools to LLM (NEW METHOD)
# llm_with_tools = llm.bind_tools(tools)

# # Query
# query = "Explain recent advancements in quantum computing"

# # Run
# response = llm_with_tools.invoke(query)

# print("\n🧠 FINAL ANSWER:\n")
# print(response.content)


import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# ✅ Increased tokens
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model="mistralai/mixtral-8x7b-instruct",
    temperature=0,
    max_tokens=1000
)

search = DuckDuckGoSearchRun()
tools = [search]

llm_with_tools = llm.bind_tools(tools)

query = "Explain recent advancements in quantum computing"

prompt = f"""
You are a research assistant.

Give a COMPLETE answer.
Do not cut off.

Structure:
1. Summary
2. Key Advancements
3. Future Trends

Question:
{query}
"""

response = llm_with_tools.invoke(prompt)

print("\n🧠 FINAL ANSWER:\n")
print(response.content)