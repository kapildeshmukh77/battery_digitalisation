from dataclasses import dataclass
from typing import Type

from digital_dryroom.schema import Schema


@dataclass
class Channel:
    rabbit_mq_que_name: str
    static_schema: Type[Schema]
    time_series_schema: Type[Schema]