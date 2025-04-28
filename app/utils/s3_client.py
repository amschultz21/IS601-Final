import boto3
from botocore.client import Config
from app.dependencies import get_settings

settings = get_settings()

s3_client = boto3.client(
    "s3",
    endpoint_url=settings.minio_endpoint,
    aws_access_key_id=settings.minio_access_key,
    aws_secret_access_key=settings.minio_secret_key,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

def upload_file_to_minio(file_data, filename, content_type):
    bucket_name = "profile-pictures"
    s3_client.upload_fileobj(
        file_data,
        bucket_name,
        filename,
        ExtraArgs={"ContentType": content_type}
    )
    return f"{settings.minio_public_url}/{bucket_name}/{filename}"
