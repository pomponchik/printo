from typing import Tuple, Dict, Callable, Any


def descript_data_object(
    class_name: str,
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
    serializator: Callable[[Any], str] = repr,
) -> str:
    args_description_chunks = []
    for argument in args:
        args_description_chunks.append(serializator(argument))
    args_description: str = ', '.join(args_description_chunks)

    kwargs_description = []
    for argument_name, value in kwargs.items():
        kwargs_description.append(f'{argument_name}=' + serializator(value))
    kwargs_description: str = ', '.join(kwargs_description_chunks)

    breackets_content = ', '.join(
        [x for x in (args_description, kwargs_description) if x]
    )

    return f'{class_name}({breackets_content})'
