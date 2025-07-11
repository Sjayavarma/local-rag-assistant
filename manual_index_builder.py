import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Step 1: Example chunks (pretend this is from PDF)
chunks = [
    "FAISS is a library for efficient similarity search.",
    "It is developed by Facebook AI.",
    "FAISS supports fast retrieval of dense vectors.",
    "This is useful for search engines and RAG systems.",
    "Sentence transformers create embeddings from text.",
]

# Step 2: Load model (will download if needed)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 3: Embed the chunks
embeddings = model.encode(chunks)

# Step 4: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Step 5: Make output folder
os.makedirs("faiss_index", exist_ok=True)

# Step 6: Save FAISS index and chunks
faiss.write_index(index, "faiss_index/index.faiss")
np.save("faiss_index/chunks.npy", chunks)

print("✅ FAISS index and chunk vectors saved successfully.")
