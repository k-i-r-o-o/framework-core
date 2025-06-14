# tests/test_vector_store_factory.py

import pytest
from core.connectors.vector_stores.factory import (
    get_vector_store,
    VECTOR_STORE_REGISTRY,
    register_vector_store
)
from core.connectors.vector_stores.qdrant import QdrantStore
from core.connectors.vector_stores.chroma import ChromaStore
from core.interfaces.store.vector_store import IVectorStore


# Register the vector stores before running tests
register_vector_store("qdrant", QdrantStore)
register_vector_store("chroma", ChromaStore)


def test_qdrant_store_registration_and_loading():
    config = {"type": "qdrant", "host": "localhost", "port": 6333}
    store = get_vector_store(config)

    assert isinstance(store, IVectorStore)
    assert store.__class__.__name__ == "QdrantStore"


def test_chroma_store_registration_and_loading():
    config = {"type": "chroma", "path": "/tmp/db"}
    store = get_vector_store(config)

    assert isinstance(store, IVectorStore)
    assert store.__class__.__name__ == "ChromaStore"


def test_invalid_backend_raises_error():
    config = {"type": "unknownstore"}

    with pytest.raises(ValueError) as exc_info:
        get_vector_store(config)

    assert "Unknown vector store type" in str(exc_info.value)
