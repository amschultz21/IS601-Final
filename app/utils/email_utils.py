import smtplib
from email.mime.text import MIMEText
from app.dependencies import get_settings

settings = get_settings()

def send_email(to: str, subject: str, body: str):
    """
    Send an email using SMTP server settings from config.
    """
    if not settings.email_enabled:
        print(f"[Email Disabled] Would send to: {to} | Subject: {subject}")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.smtp_username
    msg["To"] = to

    try:
        with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as server:
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.sendmail(settings.smtp_username, [to], msg.as_string())
            print(f"Email sent to {to} with subject '{subject}'")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise
