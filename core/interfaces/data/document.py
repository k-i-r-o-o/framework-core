# core/interfaces/data/document.py

from abc import ABC, abstractmethod
from typing import Dict, Any

class IDocument(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_content(self) -> str:
        pass

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        pass
