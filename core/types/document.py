from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Document:
    id: str
    text: str
    metadata: Dict[str, Any]

    def get_id(self) -> str:
        return self.id

    def get_content(self) -> str:
        return self.text

    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata
