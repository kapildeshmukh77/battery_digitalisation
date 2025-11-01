from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from digital_dryroom.schema.schema import Schema


@dataclass
class BFMTimeSeries(Schema):
    __table_name__ = 'bfm_timeseries'
    __time_series__ = True

    timestamp: datetime
    auto_start: Optional[bool] = None
    actual_velocity_mould: Optional[float] = None
    actual_position_mould: Optional[float] = None


@dataclass
class BFMStatic(Schema):
    __table_name__ = 'bfm_static'
    __time_series__ = False

    timestamp: datetime
    blister_count_total: Optional[float] = None
    blister_count_reset: Optional[float] = None
    last_forming_force: Optional[float] = None
    area_pouch_hold_down: Optional[float] = None
    pressure_holding_down: Optional[float] = None
    force_holding_down: Optional[float] = None
    acceleration_mould_open: Optional[float] = None
    acceleration_mould_close: Optional[float] = None
    deacceleration_mould_open: Optional[float] = None
    deacceleration_mould_close: Optional[float] = None
    position_mould_open: Optional[float] = None
    position_mould_close: Optional[float] = None
    velocity_mould_open: Optional[float] = None
    velocity_mould_close: Optional[float] = None
    acceleration_pouchfilm: Optional[float] = None
    deacceleration_pouchfilm: Optional[float] = None
    length_pouchfilm: Optional[float] = None
    velocity_pouchfilm: Optional[float] = None
    mould_pressure: Optional[float] = None