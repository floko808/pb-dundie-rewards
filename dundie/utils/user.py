from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8):
    """generate a simple random password"""
    return "".join(sample(ascii_letters + digits, size))
