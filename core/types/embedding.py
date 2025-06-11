from dataclasses import dataclass
from typing import List

@dataclass
class Embedding:
    vector: List[float]
    model: str
