import re
import smtplib
from email.mime.text import MIMEText

from dundie.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT
from dundie.utils.log import get_logger

log = get_logger()

regex = r"\b[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.\w{2,}\b"


def check_valid_email(address):
    """Return true if emil is valid"""

    return bool(re.fullmatch(regex, address))


def send_email(from_, to, subject, text):
    if not isinstance(to, list):  # guard
        # raise ValueError("to must be a list")
        to = [to]
    try:
        with smtplib.SMTP(
            host=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT
        ) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to)
            server.sendmail(from_, to, subject, message.as_string())
    except Exception:
        log.error("Cannot send email to %s", to)
