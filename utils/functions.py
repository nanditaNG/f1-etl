import pandas as pd
import boto3
from utils.models import settings, Settings

s3_client = boto3.client('s3')

def write_to_s3(local_path: str, bucket: str, key:str) -> None:
    s3_client.upload_file(Filename=local_path, Bucket=bucket, Key=key)

