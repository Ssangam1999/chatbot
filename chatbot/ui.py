import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Chatbot", page_icon="💬")

st.title("💬 LangGraph Chatbot")
st.markdown("Ask any question, and the chatbot will answer based on vector store context.")

# Input from user
user_input = st.text_input("Enter your query", "")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            # Call FastAPI backend
            response = requests.post(
                "http://localhost:8000/api/users/",
                json={"query": user_input}
            )
            if response.status_code == 200:
                data = response.json()
                st.markdown("### 🤖 Answer:")
                st.write(data.get("answer", "No answer generated."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to FastAPI backend.\n\n{e}")
