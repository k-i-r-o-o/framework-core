from core.interfaces.store.vector_store import IVectorStore
from typing import List, Dict, Any

class ChromaStore(IVectorStore):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # init chromadb client here

    def add_document(self, document: Dict[str, Any]) -> None:
        print("Chroma: adding document")

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        print("Chroma: searching")
        return []

    def delete(self, doc_id: str) -> None:
        print("Chroma: deleting document")

    
    def delete_all(self):
        print("Chroma: deleting All document")
        pass
    
from core.connectors.vector_stores.factory import register_vector_store
register_vector_store("chroma", ChromaStore)