from .common import start_message
from .match import new_match

handlers = [
    start_message,
    new_match
]

__all__ = ["handlers"]
