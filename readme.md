# Local LLM with RAG

<p align="center">
    <img src="images/wizard_experimenting.jpg" alt="A wizard experimenting - Leonardo AI" width="600">
</p>

This project demonstrates how to run local Large Language Models (LLMs) with [Ollama](https://ollama.ai/) to perform Retrieval-Augmented Generation (RAG) for answering questions based on sample PDFs. We also utilize Ollama for creating embeddings with [nomic-embed-text](https://ollama.com/library/nomic-embed-text), which are stored in [Chroma](https://docs.trychroma.com/).

[![asciicast](https://asciinema.org/a/fepTvXf1UiDpRUhhNiswL8isu.svg)](https://asciinema.org/a/fepTvXf1UiDpRUhhNiswL8isu)

A web UI has also been built using [Streamlit](https://streamlit.io/) to provide an interactive way to interact with Ollama.

<p align="center">
    <img src="images/streamlit_ui.png" alt="Screenshot of Streamlit web UI" width="600">
</p>

## Requirements

- [Ollama](https://ollama.ai/) (Ensure it is installed and running)
- Python 3.9+
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/local-llm-rag.git
cd local-llm-rag
```

### 2. Create a Virtual Environment

#### **On Ubuntu/Linux**

```sh
python3 -m venv venv
source venv/bin/activate
```

#### **On Windows (Command Prompt)**

```sh
python -m venv venv
venv\Scripts\activate
```

#### **On Windows (PowerShell)**

```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

```

## Running the Streamlit UI

Launch the Streamlit web UI by running:

```sh
streamlit run src/main.py
```

## Technologies Used

- [LangChain](https://github.com/langchain/langchain) - A Python library for working with Large Language Models
- [Ollama](https://ollama.ai/) - A platform for running Large Language Models locally
- [Chroma](https://docs.trychroma.com/) - A vector database for storing and retrieving embeddings
- [PyPDF](https://pypi.org/project/PyPDF2/) - A Python library for reading and manipulating PDF files
- [Streamlit](https://streamlit.io/) - A web framework for creating interactive applications for machine learning and data science projects

