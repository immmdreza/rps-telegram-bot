from .common import start_message
from .match import new_match, join_match

handlers = [
    start_message,
    new_match,
    join_match
]

__all__ = ["handlers"]
