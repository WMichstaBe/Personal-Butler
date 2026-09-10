from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="qwen3.5:9b",
    base_url="http://localhost:11434/v1",
    api_key="wx",
    temperature=0.7
)