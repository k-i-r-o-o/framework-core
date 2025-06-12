# core/types/document.py

from typing import Dict, Any
from pydantic import BaseModel, Field
from core.interfaces.data.document import IDocument


class Document(BaseModel, IDocument):
    id: str = Field(..., description="Unique identifier for the document")
    text: str = Field(..., description="Content of the document")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata associated with the document")

    def get_id(self) -> str:
        """Return the unique identifier of the document."""
        return self.id

    def get_content(self) -> str:
        """Return the content/text of the document."""
        return self.text

    def get_metadata(self) -> Dict[str, Any]:
        """Return the metadata dictionary."""
        return self.metadata
