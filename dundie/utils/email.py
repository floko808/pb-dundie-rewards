import re

regex = r"\b[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.\w{2,}\b"


def check_valid_email(address):
    """Return true if emil is valid"""

    return bool(re.fullmatch(regex, address))
