# core/connectors/vector_stores/registry.py

from core.config.config_loader_factory import get_config_loader
from core.connectors.vector_stores.factory import get_vector_store

def build_vector_store(source: str = "dynamo", key: str = "vector-store"):
    """
    Builds a vector store using the specified config loader source (e.g., 'dynamo', 'yaml').
    :param source: The source of the config, e.g., 'dynamo', 'yaml', 'azure'
    :param key: The config key to load (file path for yaml, key name for cloud)
    """
    loader = get_config_loader(source)
    config = loader.load(key)
    return get_vector_store(config)
