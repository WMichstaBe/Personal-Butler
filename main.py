import os
import json
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from agent.graph import build_graph
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()
DB_URI = os.getenv("POSTGRES_URI")

def get_thread_id():
    try:
        with open("thread_id.json","r",encoding="utf-8") as f:
            config = json.load(f)

        return config["thread_id"]
    except (FileNotFoundError,KeyError):#第一个是文件不存在,第二个是json文件中没有thread_id键
        import uuid
        thread_id = str(uuid.uuid4())#生成uuid作为线程id
        with open("thread_id.json","w",encoding="utf-8") as f:
            json.dump(
                {"thread_id":thread_id},
                f,
                ensure_ascii=False,
                indent=4
            )
            return thread_id

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()
    graph = build_graph(checkpointer)
    thread_id = get_thread_id()
    while True:
        user_input = input("\nuser:")

        result = graph.invoke(
            {
                "messages":[
                    HumanMessage(content=user_input)
                ]
            },
            config={
                    "configurable":{
                        "thread_id":thread_id
                    }
            }
        )
    

