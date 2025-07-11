# local-rag-assistant
 DRIVE LINK TO ACEES OTHER FILE -- https://drive.google.com/drive/folders/1lq5AoDNSy-k4Ni9FbNSKba9xmQ59v_Kp?usp=sharing
A fully offline AI assistant that answers questions from PDFs using a local RAG pipeline with Mistral 7B, LangChain, FAISS, and Streamlit — no cloud, no API, privacy-first.

# 🧠 Local RAG Assistant – Offline PDF Question Answering

🚀 A fully offline, privacy-safe AI assistant that answers questions from your PDFs using a Retrieval-Augmented Generation (RAG) pipeline with **Mistral 7B**, **FAISS**, and a clean **Streamlit UI**.

🔗 GitHub Repo: [https://github.com/Sjayavarma/local-rag-assistant](https://github.com/Sjayavarma/local-rag-assistant)

---

## 📖 Project Description

This project is a local, API-free AI assistant that enables you to ask questions from your own PDF documents — all without sending any data to the cloud. It uses a Retrieval-Augmented Generation (RAG) architecture that combines **smart document chunking**, **semantic search**, and **local language generation** using `llama.cpp` and Mistral 7B.

Built to overcome the restrictions of cloud tools like AWS and OpenAI (cost, API limits, data privacy), this system gives you full control over your documents and inference — ideal for academic papers, internal reports, resumes, legal documents, and more.

---

## 🔄 RAG Pipeline Flow

1. **📄 Upload PDF** – Load your document into the app.
2. **✂️ Chunking** – LangChain splits the document into clean, digestible sections.
3. **🧠 Embedding** – Sentence-transformers embed each chunk as vectors.
4. **⚡ Retrieval** – FAISS finds the most relevant chunks based on your query.
5. **🤖 Generation** – Mistral 7B (via llama.cpp) generates answers with that context.

---

## 🔍 Features

- 📂 Upload PDF files through a Streamlit interface
- 📎 Automatic text extraction and chunking
- 🧠 Semantic search using `sentence-transformers` + FAISS
- 🤖 Offline answer generation using Mistral 7B + llama.cpp
- 🔐 Zero cloud dependencies – fully private and local
- 🎛️ Modern UI built with Streamlit

---

## 🧰 Tech Stack

| Layer        | Tool/Library                    |
|--------------|---------------------------------|
| UI           | Streamlit                       |
| Chunking     | LangChain                       |
| Embeddings   | `sentence-transformers`         |
| Vector Store | FAISS                           |
| LLM Engine   | `llama.cpp` + Mistral 7B `.gguf`|
| PDF Parser   | PyPDF2                          |
| Language     | Python 3.10+                    |

---

## 📦 Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/Sjayavarma/local-rag-assistant.git
cd local-rag-assistant
#############2. Install Python dependencies
pip install -r requirements.txt
############3. Download the Mistral model
Download .gguf file from Hugging Face:
👉 https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

Recommended file: mistral-7b-instruct-v0.1.Q4_K_M.gguf

Place it inside the models/ folder:

mkdir models
######### Place your GGUF file here
4. Build llama.cpp (Windows)
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -A x64 -DLLAMA_CURL=ON .
cmake --build build --config Release
Or use a precompiled binary if available.

#################▶️ Run the App
streamlit run app.py
Then open your browser at: http://localhost:8501

📸 Screenshots
Upload PDF	Chat With Docs

✨ What I Learned
 ------ ( How to orchestrate a RAG pipeline locally

Working with embeddings and FAISS indexing

Building Streamlit UIs with authentication and chat flow

Running large models locally via llama.cpp ) 

🛡️ License
This project is licensed under the MIT License.

🤝 Contribution
Found a bug? Have an idea?
Feel free to fork, submit PRs, or raise issues. Collaboration is welcome!

🔗 Author
Built with ❤️ by Jayavarma S
📧 Contact: sjayavarmas@gmail.com




