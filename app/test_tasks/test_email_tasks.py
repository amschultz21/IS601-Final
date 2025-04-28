from unittest.mock import patch
from app.tasks.email_tasks import send_email_task

def test_send_email_success(monkeypatch):
    email_data = {"to": "test@example.com", "subject": "Test", "body": "Hello"}

    with patch("app.tasks.email_tasks.EmailService.send_email_sync") as mock_send, \
         patch("app.tasks.email_tasks.send_kafka_log") as mock_log:
        send_email_task(email_data)
        mock_send.assert_called_once_with("test@example.com", "Test", "Hello")
        mock_log.assert_called_with({
            "event": "email_sent",
            "status": "success",
            "recipient": "test@example.com",
            "subject": "Test"
        })

def test_send_email_failure(monkeypatch):
    email_data = {"to": "test@example.com", "subject": "Test", "body": "Hello"}

    with patch("app.tasks.email_tasks.EmailService.send_email_sync", side_effect=Exception("fail")), \
         patch("app.tasks.email_tasks.send_kafka_log") as mock_log:
        try:
            send_email_task(email_data)
        except Exception:
            pass
        mock_log.assert_called_with({
            "event": "email_sent",
            "status": "failure",
            "error": "fail",
            "recipient": "test@example.com",
            "subject": "Test"
        })
