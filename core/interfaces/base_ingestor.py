# core/interfaces/base_ingestor.py
from abc import ABC, abstractmethod

class BaseIngestor(ABC):
    @abstractmethod
    def ingest(self, source: str) -> list:
        pass
