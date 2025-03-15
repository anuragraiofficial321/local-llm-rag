import streamlit as st
import os
from langchain_ollama import ChatOllama
from document_loader import load_documents_into_database
from llm.llm import getStreamingChain

#--------------------------Constants----------------------#
CHAT_MODEL = "mistral"
EMBEDDING_MODEL = "nomic-embed-text"
TEMP_UPLOAD_DIR = "uploaded_docs"

#-----------------------Streamlit Title-----------------------#
st.title("Local LLM with RAG 📚")

#-----------------------Initialize session state-----------------------#
if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = CHAT_MODEL
    st.session_state["llm"] = ChatOllama(model=CHAT_MODEL)
if "db" not in st.session_state:
    st.session_state.db = None
if "messages" not in st.session_state:
    st.session_state.messages = []

#-----------------------File Uploader-----------------------#
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(TEMP_UPLOAD_DIR, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File {uploaded_file.name} uploaded successfully!")
    with st.spinner("Creating embeddings and loading documents into Chroma..."):
        st.session_state.db = load_documents_into_database(EMBEDDING_MODEL, TEMP_UPLOAD_DIR,uploaded_file.name,reload=True)

    st.success("Document indexed! You can now ask questions.")

#-----------------------Display chat messages from history-----------------------#
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#-----------------------Chat interface-----------------------#
if st.session_state.db is None:
    st.warning("Please upload and index a document first.")
else:
    prompt = st.chat_input("Ask a question about the document")
    if prompt:
        st.session_state.db = load_documents_into_database(EMBEDDING_MODEL, TEMP_UPLOAD_DIR,uploaded_file.name,reload=False)
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = getStreamingChain(
                prompt,
                st.session_state.messages,
                st.session_state.llm,
                st.session_state.db,
            )
            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
