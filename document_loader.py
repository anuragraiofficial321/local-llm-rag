import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from typing import List
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

def load_documents_into_database(model_name: str, documents_path: str,PERSIST_DIRECTORY,reload: bool = False) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """
    if reload:
        print("Loading documents")
        raw_documents = load_documents(documents_path)
        documents = TEXT_SPLITTER.split_documents(raw_documents)

        print("Creating embeddings and loading documents into Chroma")
        return Chroma.from_documents(
            documents=documents,
            embedding=OllamaEmbeddings(model=model_name),
            persist_directory=PERSIST_DIRECTORY
        )
    else:
        return Chroma(
            embedding_function=OllamaEmbeddings(model=model_name),
            persist_directory=PERSIST_DIRECTORY
        )


def load_documents(path: str) -> List[Document]:
    """
    Loads documents from the specified directory path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified path does not exist: {path}")

    loaders = {
        ".pdf": DirectoryLoader(
            path,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True,
            use_multithreading=True,
        ),
        ".md": DirectoryLoader(
            path,
            glob="**/*.md",
            loader_cls=TextLoader,
            show_progress=True,
        ),
    }

    docs = []
    for file_type, loader in loaders.items():
        print(f"Loading {file_type} files")
        docs.extend(loader.load())
    return docs
