from sentence_transformers import SentenceTransformer

# Load model globally to avoid reloading per request
model = SentenceTransformer("all-MiniLM-L6-v2")  # or any other suitable model

def get_embedding(text: str) -> list[float]:
    embedding = model.encode(text, normalize_embeddings=True)  # normalize = cosine sim
    return embedding.tolist()