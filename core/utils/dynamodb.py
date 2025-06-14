# core/utils/dynamodb.py

from boto3.dynamodb.types import TypeDeserializer

def deserialize_item(item: dict) -> dict:
    """
    Converts DynamoDB item structure to a normal Python dictionary.
    """
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in item.items()}
