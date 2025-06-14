import os

# Set logging env vars here if not set in shell
# os.environ["LOG_FORMAT"] = "json"
os.environ["LOG_LEVEL"] = "DEBUG"

from core.config.loaders.dynamo_loader import DynamoDBConfigLoader

if __name__ == "__main__":
    loader = DynamoDBConfigLoader(table_name="surya-ddb-table-config")
    config = loader.load("sp:common:interaction")
    print("Loaded Config:", config)  # or use logger here if desired
