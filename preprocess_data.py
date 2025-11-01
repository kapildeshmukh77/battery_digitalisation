from dataclasses import asdict
from datetime import datetime
from typing import Union, Tuple, Type

from digital_dryroom.schema import Schema


def reformat_data(data_as_list: list,
                  static_schema: Type[Schema],
                  time_series_schema: Type[Schema]) -> Tuple[dict, dict]:
    """
    1. Assigns data either to static or time series map depending on postfix
    2. Removes postfix from the name to match fieldnames of the database table
    3. Does custom data handling for special fields like "position_mould" which contains multiple values
    """
    static_data = {}
    time_series_data = {}

    for entry in data_as_list:
        try:
            if entry['browseName'].endswith("?static"):
                table_field_name = entry['browseName'].replace("?static", "")
                value = _cast_to_bool_or_float(entry['value'])
                static_data[table_field_name] = value

            if entry['browseName'].endswith("?timeseries"):
                table_field_name = entry['browseName'].replace("?timeseries", "")
                value = _cast_to_bool_or_float(entry['value'])
                time_series_data[table_field_name] = value
        except Exception as exc:
            # failing quietly while parsing.
            print(f"Wooops, failing quietly while parsing: {exc}.")

    # Assign timestamp from the first entry
    timestamp = datetime.strptime(data_as_list[0]['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    time_series_data['timestamp'] = timestamp
    static_data['timestamp'] = timestamp

    static_data = _validate_and_fix(static_schema, static_data)
    time_series_data = _validate_and_fix(time_series_schema, time_series_data)

    return static_data, time_series_data

def _validate_and_fix(schema: Type[Schema], data: dict) -> dict:
    # This would fail if the data would differ from what is expected by the schema!
    # We are doing the back and forth converting as we implement methods to fix missing data inside the schema!
    data_as_schema = schema.from_dict(data)
    return asdict(data_as_schema)


def _cast_to_bool_or_float(value) -> Union[bool, float]:
    return value if isinstance(value, bool) else float(value)
