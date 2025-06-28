from chatbot.services.chat_services import ChatEngine


if __name__ == "__main__":
    chat_obj = ChatEngine()
    query = "What is the document about?"
    result = chat_obj.run({"query": query})
    print(result["answer"])
