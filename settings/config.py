from pydantic import Field, AnyUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    max_login_attempts: int = Field(default=3)
    server_base_url: AnyUrl = Field(default='http://localhost')
    server_download_folder: str = Field(default='downloads')

    secret_key: str = Field(default="supersecretkey")
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=15)
    refresh_token_expire_minutes: int = Field(default=1440)
    admin_user: str = Field(default='admin')
    admin_password: str = Field(default='secret')
    debug: bool = Field(default=False)
    jwt_secret_key: str = "a_very_secret_key"
    jwt_algorithm: str = "HS256"

    database_url: str = Field(default='postgresql+asyncpg://user:password@localhost/myappdb')

    # Mail settings
    smtp_server: str = Field(default='smtp.mailtrap.io')
    smtp_port: int = Field(default=2525)
    smtp_username: str = Field(default='your-mailtrap-username')
    smtp_password: str = Field(default='your-mailtrap-password')
    email_enabled: bool = Field(default=True)
    send_real_mail: bool = Field(default=False)

    # Kafka Settings
    kafka_bootstrap_servers: str = Field(default="localhost:9092")
    kafka_email_topic: str = Field(default="email-topic")

    # Minio settings
    minio_endpoint: str = Field(default="http://localhost:9000")
    minio_access_key: str = Field(default="minioadmin")
    minio_secret_key: str = Field(default="minioadmin")
    minio_bucket_name: str = Field(default="profile-pictures")
    minio_public_url: str = Field(default="http://localhost:9000")
    # Add to Settings class
    minio_root_user: str = Field(default="minioadmin")
    minio_root_password: str = Field(default="minioadmin")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow",  # 👈 this lets you keep POSTGRES_* in .env without crashing
    }


# Singleton pattern to reuse config
settings = Settings()
