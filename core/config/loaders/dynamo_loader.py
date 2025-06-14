# core/config/loaders/dynamo_loader.py

import json
from core.telemetry.logger import get_logger
from core.telemetry.decorators import auto_log_class
from core.config.clients.aws_client import get_boto3_client
from core.utils.dynamodb import deserialize_item  # 👈 new import

logger = get_logger(__name__)

@auto_log_class
class DynamoDBConfigLoader:
    def __init__(self, table_name: str = "surya-ddb-table-config"):
        self.table_name = table_name
        self.client = get_boto3_client("dynamodb")

    def load(self, key: str) -> dict:
        response = self.client.get_item(
            TableName=self.table_name,
            Key={"id": {"S": key}},
        )
        logger.info(f"Response from DynamoDB: {(response)}")
        item = response.get("Item")
        if not item:
            raise ValueError(f"No config found for key: {key}")

        # ✅ Deserialize entire item
        deserialized_item = deserialize_item(item)

        try:
            config = deserialized_item["data"]  
            return {
                "key": key,
                "config": config,
            }
        except KeyError as e:
            logger.error(f"Expected 'data' field not found: {e}")
            raise ValueError(f"Invalid item structure for key: {key}")
