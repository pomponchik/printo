from typing import Tuple, Dict, Callable, Union, Optional, Any

from printo.reprs import superrepr


def descript_data_object(
    class_name: str,
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
    serializator: Callable[[Any], str] = superrepr,
    filters: Optional[Dict[Union[str, int], Callable[[Any], bool]]] = None,
) -> str:
    real_filters: Dict[Union[str, int], Callable[[Any], bool]] = (
        filters if filters is not None else {}
    )

    args_description_chunks = []
    for index, argument in enumerate(args):
        filter = real_filters.get(index, lambda x: True)
        if filter(argument):
            args_description_chunks.append(serializator(argument))
    args_description: str = ', '.join(args_description_chunks)

    kwargs_description_chunks = []
    for argument_name, value in kwargs.items():
        filter = real_filters.get(argument_name, lambda x: True)
        if filter(value):
            kwargs_description_chunks.append(f'{argument_name}=' + serializator(value))
    kwargs_description: str = ', '.join(kwargs_description_chunks)

    breackets_content = ', '.join(
        [x for x in (args_description, kwargs_description) if x]
    )

    return f'{class_name}({breackets_content})'
