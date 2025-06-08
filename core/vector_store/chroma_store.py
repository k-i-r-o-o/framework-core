# core/vector_store/chroma_store.py
from core.vector_store.base_store import BaseVectorStore

class ChromaVectorStore(BaseVectorStore):
    def __init__(self):
        self.data = []

    def add(self, embedding: list, metadata: dict):
        self.data.append((embedding, metadata))

    def search(self, query_embedding: list, top_k: int = 5):
        # Dummy implementation
        return self.data[:top_k]
