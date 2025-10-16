from typing import Tuple, Dict, Callable, Union, Optional, Any

from printo.reprs import superrepr


def descript_data_object(
    class_name: str,
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
    serializator: Callable[[Any], str] = superrepr,
    filters: Optional[Dict[Union[str, int], Callable[[Any], bool]]] = None,
    placeholders: Optional[Dict[Union[str, int], str]] = None,
) -> str:
    real_filters: Dict[Union[str, int], Callable[[Any], bool]] = (
        filters if filters is not None else {}
    )
    get_placehlder: Callable[[Union[str, int]], Optional[str]] = lambda field_name: placeholders.get(field_name) if placeholders is not None else None

    args_description_chunks = []
    for index, argument in enumerate(args):
        filter = real_filters.get(index, lambda x: True)
        if filter(argument):
            placeholder = get_placehlder(index)
            if placeholder is not None:
                serialized_value = placeholder
            else:
                serialized_value = serializator(argument)
            args_description_chunks.append(serialized_value)
    args_description: str = ', '.join(args_description_chunks)

    kwargs_description_chunks = []
    for argument_name, value in kwargs.items():
        filter = real_filters.get(argument_name, lambda x: True)
        if filter(value):
            placeholder = get_placehlder(argument_name)
            if placeholder is not None:
                serialized_value = placeholder
            else:
                serialized_value = serializator(value)
            kwargs_description_chunks.append(f'{argument_name}=' + serialized_value)
    kwargs_description: str = ', '.join(kwargs_description_chunks)

    breackets_content = ', '.join(
        [x for x in (args_description, kwargs_description) if x]
    )

    return f'{class_name}({breackets_content})'
