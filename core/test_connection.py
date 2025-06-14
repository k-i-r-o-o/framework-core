# test_connection.py

from config.aws_client import get_boto3_client

if __name__ == "__main__":
    get_boto3_client("dynamodb")
