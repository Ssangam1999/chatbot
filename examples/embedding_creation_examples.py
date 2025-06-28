from chatbot.services.embedding_services import DocumentProcessor

if __name__ == "__main__":
    embedding_obj = DocumentProcessor()
    embedding_obj.run_all()