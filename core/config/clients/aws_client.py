# core/config/aws_client.py

import boto3
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


def get_boto3_client(service_name: str, region_name: str = "eu-north-1"):
    region = region_name or os.getenv("AWS_REGION", "eu-north-1")

    client = boto3.client(
        service_name,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=region,
    )

    # Optional test
    if service_name == "dynamodb":
        try:
            client.list_tables()
            print("Connected to DynamoDB")
        except Exception as e:
            print(f"Error connecting to DynamoDB: {e}")
            return None

    return client

 