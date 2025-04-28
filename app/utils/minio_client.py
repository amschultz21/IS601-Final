from minio import Minio
from app.dependencies import get_settings

settings = get_settings()

minio_client = Minio(
    "localhost:9000",
    access_key=settings.minio_root_user,
    secret_key=settings.minio_root_password,
    secure=False
)

bucket_name = "profile-pictures"

def ensure_bucket_exists():
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
