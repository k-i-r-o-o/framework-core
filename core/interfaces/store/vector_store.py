from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IVectorStore(ABC):
    @abstractmethod
    def add_document(self, document: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete(self, doc_id: str) -> None:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass