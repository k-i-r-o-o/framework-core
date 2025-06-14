# core/interfaces/config/config_loader.py

from abc import ABC, abstractmethod
from typing import Dict, Any

class IConfigLoader(ABC):
    @abstractmethod
    def load(self, key_or_path: str) -> Dict[str, Any]:
        pass
