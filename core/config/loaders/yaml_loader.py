# core/config/loaders/yaml_loader.py

import yaml
from core.interfaces.config.config_loader import IConfigLoader

class YAMLConfigLoader(IConfigLoader):
    def load(self, path: str) -> dict:
        with open(path, "r") as f:
            return yaml.safe_load(f)
