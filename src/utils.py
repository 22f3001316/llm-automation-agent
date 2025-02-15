import os
from pathlib import Path

DATA_DIR = Path("/data")

def write_file(path, content):
    with open(DATA_DIR / path, "w", encoding="utf-8") as f:
        f.write(content)

def read_file(path):
    with open(DATA_DIR / path, "r", encoding="utf-8") as f:
        return f.read()

def find_most_similar(comments):
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(comments, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(embeddings, embeddings)
    most_similar_idx = scores.argmax().item()
    return [comments[most_similar_idx], comments[most_similar_idx - 1]]
