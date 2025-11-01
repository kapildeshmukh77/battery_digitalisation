from datetime import datetime
from typing import get_origin, Union, get_args


def python_type_to_sql(py_type):
    # Handle Optional[T] (which is Union[T, NoneType])
    if get_origin(py_type) is Union:
        args = [arg for arg in get_args(py_type) if arg is not type(None)]
        if len(args) == 1:
            py_type = args[0]  # unwrap Optional[T]

    if py_type == float:
        return "DOUBLE PRECISION"
    elif py_type == int:
        return "INTEGER"
    elif py_type == bool:
        return "BOOLEAN"
    elif py_type == str:
        return "TEXT"
    elif py_type == datetime:
        return "TIMESTAMPTZ"
    else:
        raise ValueError(f"Unsupported type: {py_type}")