import os
import numpy as np
import faiss
import subprocess
from pathlib import Path
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Constants
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
INDEX_PATH = "faiss_index/index.faiss"
CHUNK_STORE = "faiss_index/chunks.npy"
MODEL_PATH = "D:/RAG/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"



# ✅ Update this path to match your real compiled executable
LLAMA_EXECUTABLE = "D:/RAG/llama.cpp/build/bin/Release/llama-run.exe"
  # <- Corrected

def load_and_process_docs(uploaded_files):
    all_text = ""
    os.makedirs("docs", exist_ok=True)

    for uploaded in uploaded_files:
        file_path = Path("docs") / uploaded.name
        with open(file_path, "wb") as f:
            f.write(uploaded.getbuffer().read())
        print(f"📥 Saved PDF: {file_path}")

        try:
            reader = PdfReader(str(file_path))
            for page_num, page in enumerate(reader.pages):
                try:
                    text = page.extract_text()
                    if text:
                        all_text += text + "\n"
                except Exception as e:
                    print(f"⚠️ Skipping unreadable page {page_num}: {e}")
        except Exception as e:
            print(f"❌ Could not open PDF: {file_path.name} — {e}")
            continue

    if not all_text.strip():
        print("❌ No text extracted from PDF.")
        return

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_text(all_text)
    print(f"📄 Total Chunks: {len(chunks)}")

    # Create embeddings
    print("🧠 Generating embeddings...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    vectors = model.encode(chunks, show_progress_bar=True)

    # Create FAISS index
    print("📦 Creating FAISS index...")
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))

    os.makedirs("faiss_index", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    np.save(CHUNK_STORE, chunks)
    print("✅ Index and chunks saved.")

def answer_query(query):
    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNK_STORE):
        return "❌ Please upload and process documents first."

    print("🔎 Loading index and chunks...")
    index = faiss.read_index(INDEX_PATH)
    chunks = np.load(CHUNK_STORE, allow_pickle=True)

    # Query vector
    model = SentenceTransformer(EMBEDDING_MODEL)
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), k=3)
    retrieved_chunks = [chunks[i] for i in I[0]]

    context = "\n".join(retrieved_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    # ✅ Check if llama.cpp executable exists
    if not os.path.exists(LLAMA_EXECUTABLE):
        return "❌ llama.cpp executable not found. Please check the path."

    print("🧠 Running local model...")
    result = subprocess.run(
    [
        LLAMA_EXECUTABLE,
        MODEL_PATH,              # ✅ Pass model as first argument
        "-p", prompt,            # ✅ Prompt
        "-n", "300",             # ✅ Number of tokens
        "--threads", "4"         # ✅ Optional performance boost
    ],
    capture_output=True,
    text=True
)

    if result.returncode != 0:
        return f"❌ Error running llama.cpp:\n{result.stderr}"

    output = result.stdout
    return output.split("Answer:")[-1].strip()
