from pathlib import Path
from types import SimpleNamespace
from io import BytesIO
from rag_core import load_and_process_docs

pdf_path = Path("docs/test.pdf")
print(f"📝 Loading: {pdf_path.resolve()}")

if not pdf_path.exists():
    print("❌ PDF file does not exist!")
else:
    # Use BytesIO to simulate a file-like object
    def getbuffer():
        with open(pdf_path, "rb") as f:
            return BytesIO(f.read())
    
    uploaded = SimpleNamespace(name=pdf_path.name, getbuffer=getbuffer)
    print("📦 Simulated upload complete")
    
    print("🔍 Processing...")
    load_and_process_docs([uploaded])
    print("✅ Processing done")

    # Check output files
    from os.path import exists
    print("📁 Checking generated files:")
    print(" - faiss_index/index.faiss:", exists("faiss_index/index.faiss"))
    print(" - faiss_index/chunks.npy :", exists("faiss_index/chunks.npy"))
