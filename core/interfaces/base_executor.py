# core/interfaces/base_executor.py
from abc import ABC, abstractmethod

class BaseExecutor(ABC):
    @abstractmethod
    def execute(self, payload: dict) -> dict:
        pass
