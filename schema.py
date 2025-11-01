"""
Contains a central definition of our schema. The names are mirrored from Node-RED.
Important: The names must match the names from Node-RED!!!

"""
from abc import ABC
from dataclasses import dataclass
from dataclasses import fields
from typing import ClassVar, Type, Dict, Any, Tuple, List


@dataclass
class Schema(ABC):
    # Technically, all other fields of Schemas are ClassVars as we are not creating objects of the schema, but rather
    # use the schema for defining the DB-Schema. Yet we use ClassVar here to make tag "meta-information" about a
    # schema
    __table_name__: ClassVar[str] = ""
    __time_series__: ClassVar[bool] = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        annotations = getattr(cls, "__annotations__", {})
        if "timestamp" not in annotations:
            raise TypeError(f"{cls.__name__} must define a 'timestamp' field!")
        # Ensure 'timestamp' is the first field
        first_field = next(iter(annotations))
        if first_field != "timestamp":
            raise TypeError(f"In {cls.__name__}, 'timestamp' must be the first attribute so the SQL parsing is working "
                            f"correctly!")

    @classmethod
    def get_fields(cls):
        """Return all instance fields (skip ClassVars / metadata)"""
        return fields(cls)

    @classmethod
    def get_table_name(cls) -> str:
        if not cls.__table_name__:
            raise NotImplementedError("Subclasses must define __table_name__")
        return cls.__table_name__

    @classmethod
    def is_timeseries(cls) -> bool:
        return cls.__time_series__

    @classmethod
    def from_dict(cls, data: dict):
        valid_data, unknown, missing = diff_fields(cls, data)
        if unknown:
            print(f"Warning: Data has unknown fields of {cls.__name__}: {unknown}")
        if missing:
            print(f"Warning: Data misses fields of {cls.__name__}, using defaults: {missing}")

        return cls(**valid_data)

def diff_fields(schema: Type, data: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str], List[str]]:
    """
    Used to compare incoming data to a specified schema. Returns list of data which is missing, and data which is
    "additional", meaning present in the data but not in the schema.
    """
    valid_fields = {f.name for f in fields(schema)}
    data_fields = set(data.keys())

    fields_in_data_but_not_defined_in_schema = sorted(data_fields - valid_fields)
    fields_defined_by_schema_but_not_present_in_data = sorted(valid_fields - data_fields)

    valid_data = {k: v for k, v in data.items() if k in valid_fields}

    return valid_data, fields_in_data_but_not_defined_in_schema, fields_defined_by_schema_but_not_present_in_data