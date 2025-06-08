# core/vector_store/base_store.py
from abc import ABC, abstractmethod

class BaseVectorStore(ABC):
    @abstractmethod
    def add(self, embedding: list, metadata: dict):
        pass

    @abstractmethod
    def search(self, query_embedding: list, top_k: int = 5):
        pass
