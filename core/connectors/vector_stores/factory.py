from core.interfaces.stores.vector_store import IVectorStore
from core.connectors.vector_stores.chroma import ChromaVectorStore

def get_vector_store(store_type: str, config: dict) -> IVectorStore:
    if store_type == "chroma":
        return ChromaVectorStore(persist_directory=config.get("persist_directory", "./chroma_store"))
    raise ValueError(f"Unknown vector store type: {store_type}")
