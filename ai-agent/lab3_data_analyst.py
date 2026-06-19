import pandas as pd
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key
load_dotenv()

# Load CSV
df = pd.read_csv("sales.csv")

# Convert data to text
data_text = df.to_string()
# 
# Initialize Grok model (OpenAI-compatible endpoint)
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3-8b-instruct",  
    temperature=0
)

# Prompt
prompt = f"""
You are a professional data analyst.

Dataset:
{data_text}

Tasks:
1. Identify highest sales region
2. Rank all regions
3. Give short explanation

Answer clearly.
"""

# Invoke model
response = llm.invoke(prompt)

print("\n📊 ANALYSIS RESULT:\n")
print(response.content)