# core/models/embedding.py
from dataclasses import dataclass

@dataclass
class Embedding:
    vector: list
    metadata: dict
