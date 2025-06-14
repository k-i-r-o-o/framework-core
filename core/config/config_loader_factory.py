# core/config/config_loader_factory.py

from core.config.loaders.yaml_loader import YAMLConfigLoader
from core.config.loaders.dynamo_loader import DynamoDBConfigLoader
from core.interfaces.config.config_loader import IConfigLoader

def get_config_loader(source: str) -> IConfigLoader:
    if source == "yaml":
        return YAMLConfigLoader()
    elif source == "dynamo":
        return DynamoDBConfigLoader()
    # future: elif source == "azure": return AzureConfigLoader()
    else:
        raise ValueError(f"Unsupported config loader: {source}")
