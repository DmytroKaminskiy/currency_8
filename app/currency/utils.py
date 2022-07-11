import random
import string


def get_password(length: int = 10) -> str:
    """
    generate password
    """

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)

    return password
