from typing import Tuple, Dict, Callable, Any


def descript_data_object(class_name: str, args: Tuple[Any, ...], kwargs: Dict[str, Any], serializator: Callable[[Any], str] = repr) -> str:
    args_description: str = ', '.join([serializator(x) for x in args])
    kwargs_description: str = ', '.join([f'{argument_name}=' + serializator(value) for argument_name, value in kwargs.items()])

    breackets_content = ', '.join([x for x in (args_description, kwargs_description) if x])

    return f'{class_name}({breackets_content})'
