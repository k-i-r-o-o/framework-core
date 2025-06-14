from core.interfaces.store.vector_store import IVectorStore
from typing import Dict, Type, Any

# Registry to map backend names to classes
VECTOR_STORE_REGISTRY: Dict[str, Type[IVectorStore]] = {}

def register_vector_store(name: str, store_cls: Type[IVectorStore]):
    VECTOR_STORE_REGISTRY[name.lower()] = store_cls

def get_vector_store(config: Dict[str, Any]) -> IVectorStore:
    backend = config.get("type", "").lower()
    store_cls = VECTOR_STORE_REGISTRY.get(backend)

    if not store_cls:
        raise ValueError(f"Unknown vector store type: '{backend}'")

    return store_cls(config)
