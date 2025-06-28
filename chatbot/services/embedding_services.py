import os
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from chatbot.configs.embedding_model_config import embedding_model


file_path = os.path.dirname(os.path.abspath(__file__))


class DocumentProcessor:
    """
    Handles the full document processing pipeline:
    1. Load PDF
    2. Split into chunks
    3. Create embeddings
    4. Save FAISS index
    """

    def __init__(self, index_dir: str = "faiss_index"):
        """
        Initialize the processor with paths.

        :param pdf_path: Path to the input PDF file.
        :param index_dir: Directory to store the FAISS index.
        """
        self.pdf_path = os.path.join(file_path,"..","..","data","abc.pdf")
        self.index_dir = index_dir
        self.documents: List[Document] = []
        self.split_docs: List[Document] = []

    def load_documents(self) -> None:
        """
        Loads documents from a PDF file using PyPDFLoader.
        """
        loader = PyPDFLoader(self.pdf_path)
        self.documents = loader.load()

    def split_documents(self, chunk_size: int = 500, chunk_overlap: int = 100) -> None:
        """
        Splits loaded documents into smaller chunks using RecursiveCharacterTextSplitter.

        :param chunk_size: Number of characters per chunk.
        :param chunk_overlap: Number of overlapping characters between chunks.
        """
        if not self.documents:
            raise ValueError("No documents loaded. Call load_documents() first.")

        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.split_docs = splitter.split_documents(self.documents)

    def create_and_save_index(self):
        """
        Generates embeddings from the split documents and saves them to a local FAISS index.
        """
        if not self.split_docs:
            raise ValueError("No split documents. Call split_documents() first.")

        embeddings = OllamaEmbeddings(model=embedding_model)
        vectorstore = FAISS.from_documents(self.split_docs, embedding=embeddings)
        vectorstore.save_local(self.index_dir)
        return embeddings

    def run_all(self) -> None:
        """
        Runs the complete pipeline: load → split → embed → save.
        """
        self.load_documents()
        self.split_documents()
        self.create_and_save_index()


