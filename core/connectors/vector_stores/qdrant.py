from core.interfaces.store.vector_store import IVectorStore
from typing import Dict, Any

class QdrantStore(IVectorStore):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def add_document(self, document: Dict[str, Any]) -> None:
        print("Qdrant: Adding document")

    def search(self, query: str, top_k: int = 5):
        print("Qdrant: Searching")
        return []

    def delete(self, doc_id: str) -> None:
        print("Qdrant: Deleting document")

    
    def delete_all(self):
        # Dummy or real implementation
        pass


# Register with the factory
from core.connectors.vector_stores.factory import register_vector_store
register_vector_store("qdrant", QdrantStore)
