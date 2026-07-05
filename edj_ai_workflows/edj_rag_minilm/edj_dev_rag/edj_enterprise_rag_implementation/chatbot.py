import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

MODELS = {
    "1": "all-MiniLM-L6-v2",
    "2": "all-mpnet-base-v2",
    "3": "multi-qa-mpnet-base-dot-v1",
    "4": "bge-small-en-v1.5"
}

print("Choose Embedding Model\n")

for key, value in MODELS.items():
    print(f"{key}. {value}")

choice = input("\nEnter Choice : ")

model_folder = MODELS[choice]

model_name = {
    "all-MiniLM-L6-v2":"sentence-transformers/all-MiniLM-L6-v2",
    "all-mpnet-base-v2":"sentence-transformers/all-mpnet-base-v2",
    "multi-qa-mpnet-base-dot-v1":"sentence-transformers/multi-qa-mpnet-base-dot-v1",
    "bge-small-en-v1.5":"BAAI/bge-small-en-v1.5"
}[model_folder]

model = SentenceTransformer(model_name)

index = faiss.read_index(
    os.path.join("faiss_indexes",
                 model_folder,
                 "index.faiss")
)

with open(os.path.join("faiss_indexes",
                       model_folder,
                       "chunks.pkl"),"rb") as f:
    chunks = pickle.load(f)

while True:

    question = input("\nYou : ")

    if question.lower()=="exit":
        break

    query = model.encode([question])

    D,I = index.search(query.astype("float32"),3)

    print("\nRetrieved Context:\n")

    for idx in I[0]:
        print(chunks[idx])
        print("-"*60)