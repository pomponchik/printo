from typing import Any


def not_none(argument: Any) -> bool:
    if argument is None:
        return False
    return True
