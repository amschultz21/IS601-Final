from celery import Celery
from app.utils.email_utils import send_email  # your existing email function
from app.schemas.email_schema import EmailSchema  # adjust if needed
from app.utils.kafka_producer import send_kafka_log
from datetime import datetime

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # adjust Redis URL if needed
)

@celery_app.task
def send_email_task(email_data: dict):
    try:
        to = email_data["to"]
        subject = email_data["subject"]
        body = email_data["body"]

        email_service = EmailService()
        email_service.send_email_sync(to, subject, body)

        # Send success log to Kafka
        send_kafka_log({
            "event": "email_sent",
            "status": "success",
            "recipient": to,
            "subject": subject
        })

    except Exception as e:
        # Send failure log to Kafka
        send_kafka_log({
            "event": "email_sent",
            "status": "failure",
            "error": str(e),
            "recipient": email_data.get("to"),
            "subject": email_data.get("subject")
        })
        raise e  # keep original behavior
