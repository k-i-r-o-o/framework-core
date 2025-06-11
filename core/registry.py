from core.connectors.vector_stores.factory import get_vector_store
from core.config.loader import load_config

def build_vector_store():
    config = load_config("config/vector_store.yaml")
    return get_vector_store(config["type"], config["config"])
