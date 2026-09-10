from agent.graph import graph
from langchain_core.messages import HumanMessage

while True:
    user_input = input("\n先生:")

    result = graph.invoke(
        {
            "messages":[
                HumanMessage(content=user_input)
            ]
        }
    )

"""
result类似:
{
    "messages":[
        HumanMessage(content="你好"),
        AIMessage(content="先生您好，很高兴为您服务")
    ]
}

AIMessage类似:
AIMessage(
    content="先生您好，很高兴为您服务",
    id="xxx",
    response_metadata={}
)
"""