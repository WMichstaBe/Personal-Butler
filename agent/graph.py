from langgraph.graph import StateGraph,START,END
from langchain_core.messages import SystemMessage,AIMessage
from .state import MaidState
from .prompt import SYSTEM_PROMPT
from models.llm import llm


def maid_node(state: MaidState) -> MaidState:
    messages = [SystemMessage(content=SYSTEM_PROMPT)]#创建系统消息

    messages.extend(state["messages"])#添加用户消息
    
    #response = llm.invoke(messages)
    """
    这里不用response = llm.invoke(messages),因为这个要全部生成之后才返回,无法做到流式输出
    所以这里用llm.stream(messages)来实现流式输出
    """
    response_content = ""
    print("管家:", end="", flush=True)
    for chunk in llm.stream(messages):
        print(
            chunk.content,
            end="",
            flush=True
            )
        response_content += chunk.content

    response = AIMessage(content=response_content)

    return {
        "messages":[response]
    }

builder = StateGraph(MaidState)
builder.add_node("maid",maid_node)

builder.add_edge(START,"maid")
builder.add_edge("maid",END)

graph = builder.compile()