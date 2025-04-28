from kafka import KafkaProducer
from app.dependencies import get_settings

settings = get_settings()

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=settings.kafka_bootstrap_servers,
        value_serializer=lambda v: v.encode("utf-8")
    )

def send_kafka_log(log_message: dict):
    producer = get_kafka_producer()
    producer.send(settings.kafka_email_topic, value=str(log_message))
