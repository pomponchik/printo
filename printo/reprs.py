from inspect import isclass, isfunction
from typing import Any


def superrepr(value: Any) -> str:
    if isfunction(value):
        result = value.__name__

        if result == '<lambda>':
            return 'λ'

        return result

    if isclass(value):
        return value.__name__

    return repr(value)
