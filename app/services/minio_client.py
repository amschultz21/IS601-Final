from minio import Minio
from app.dependencies import get_settings

settings = get_settings()

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=False  # set True if using HTTPS
)
