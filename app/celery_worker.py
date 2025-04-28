from celery import Celery

celery_app = Celery(
    "worker",
    broker="kafka://localhost:9092",  # Placeholder: real Kafka needs additional setup
    backend="rpc://",  # or another result backend
)

celery_app.conf.task_routes = {
    "app.tasks.email.send_verification_email": {"queue": "emails"},
}
