from typing import List
from pydantic import BaseModel, Field
from core.interfaces.data.embedding import IEmbedding


class Embedding(BaseModel, IEmbedding):
    vector: List[float] = Field(..., description="Embedding vector values.")
    model_name: str = Field(..., description="Model that generated the embedding.")

    def get_vector(self) -> List[float]:
        return self.vector

    def get_model_name(self) -> str:
        return self.model_name
