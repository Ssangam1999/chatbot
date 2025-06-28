# 🏠 Landlord-Tenant Agreement Chatbot

An intelligent chatbot designed to assist with questions and information about landlord-tenant agreements. This AI-powered assistant helps users navigate rental agreement documents with ease.

## 🚀 Features

- **Document-based Q&A**: Get instant answers about landlord-tenant agreements
- **Smart Document Processing**: Powered by advanced language models
- **User-friendly Interface**: Clean Streamlit web interface
- **Customizable Models**: Easy configuration for different LLMs and embedders

## 🛠️ Technology Stack

- **LLM**: Llama3 with Ollama
- **Embedder**: nomic-embed-text
- **Frontend**: Streamlit
- **Backend**: Python

## 📋 Prerequisites

Before getting started, ensure you have the following installed:

- Python 3.12
- [uv](https://docs.astral.sh/uv/) package manager
- [Ollama](https://ollama.ai/) with Llama3 model
- nomic-embed-text embedder

> **Note**: If you have different LLM or embedding models installed, you can easily update the configuration in the `configs` file.

## 🔧 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repo>
   cd <repo>
   ```

2. **Set up virtual environment and install dependencies**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv install
   ```

## 🚀 Quick Start

Follow these steps to get the chatbot running:

1. **Start the main application**:
   ```bash
   python chatbot/main.py
   ```

2. **Launch the web interface** (in a new terminal):
   ```bash
   streamlit run chatbot/ui.py
   ```

3. **Open your browser** and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## ⚙️ Configuration

To use different models or adjust settings:

1. Navigate to the `configs` directory
2. Update the configuration files with your preferred:
   - LLM model settings
   - Embedding model parameters
   - Other application settings

## 📝 Usage

1. Upload or reference your landlord-tenant agreement document
2. Ask questions about the agreement in natural language
3. Get instant, contextual answers based on the document content
