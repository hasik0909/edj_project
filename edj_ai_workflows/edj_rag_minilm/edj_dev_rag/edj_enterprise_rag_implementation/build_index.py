import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_FOLDER = "data"
INDEX_FOLDER = "faiss_index"

models = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "sentence-transformers/all-mpnet-base-v2",
    "sentence-transformers/multi-qa-mpnet-base-dot-v1",
    "BAAI/bge-small-en-v1.5"
]

documents = []
metadata = []

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".txt"):
        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = text.split("\n\n")

        for chunk in chunks:
            if chunk.strip():
                documents.append(chunk)
                metadata.append(filename)

print(f"Total Chunks : {len(documents)}")

os.makedirs(INDEX_FOLDER, exist_ok=True)

for model_name in models:

    print("=" * 60)
    print("Building Index for:", model_name)

    model = SentenceTransformer(model_name)

    embeddings = model.encode(documents,
                              convert_to_numpy=True,
                              show_progress_bar=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    folder = os.path.join(INDEX_FOLDER, model_name.split("/")[-1])

    os.makedirs(folder, exist_ok=True)

    faiss.write_index(index,
                      os.path.join(folder, "index.faiss"))

    with open(os.path.join(folder, "chunks.pkl"), "wb") as f:
        pickle.dump(documents, f)

    with open(os.path.join(folder, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)

    print("Saved:", folder)

print("\nFinished Building All Models!")