from typing import Any
from inspect import isfunction


def superrepr(value: Any) -> str:
    if isfunction(value):
        result = value.__name__

        if result == '<lambda>':
            return 'λ'

        return result

    return repr(value)
