from fastapi import APIRouter
from langgraph.graph import StateGraph

from chatbot.schema.process_fastapi_request import ABC
from chatbot.schema.process_langraph_request import ChatState
from chatbot.services.chat_services import ChatEngine


router = APIRouter()
chat_obj = ChatEngine()


def retrieve(state):
    docs = chat_obj.retrieve_documents(state["query"])
    return {**state, "docs": docs}


def generate(state):
    answer = chat_obj.generate_answer(state["query"])
    return {**state, "answer": answer}


@router.post("/users", tags=["chatbot"])
async def read_users(query: ABC):
    graph = StateGraph(ChatState)
    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")
    graph.set_finish_point("generate")

    chatbot = graph.compile()
    response = chatbot.invoke({"query": query.query})
    return {"answer": response["answer"]}
