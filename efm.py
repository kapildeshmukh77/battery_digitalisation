
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from digital_dryroom.schema.schema import Schema


"""
General
"""

@dataclass
class EFMGeneralTimeSeries(Schema):
    __table_name__ = 'efm_general_timeseries'
    __time_series__ = True

    timestamp: datetime
    filling_running: Optional[bool] = None
    degassing_running: Optional[bool] = None
    ropex_controller_sp_actual_temperature: Optional[float] = None
    vacuum_chamber_sp_ctrl_pressure_set_point: Optional[float] = None
    vacuum_chamber_sp_chamber_pressure: Optional[float] = None

@dataclass
class EFMGeneralStatic(Schema):
    __table_name__ = 'efm_general_static'
    __time_series__ = False

    timestamp: datetime
    filling_enables_sealing_bar: Optional[bool] = None
    filling_sp_sp_sealing_vacuum: Optional[float] = None
    sealing_sp_sealing_vaccum_wait_time: Optional[float] = None
    ropex_controller_sp_sp_sealing_temperature: Optional[float] = None
    ropex_controller_sp_actual_temperature: Optional[float] = None
    sealing_sp_sp_sealing_pressure: Optional[float] = None
    sealing_sp_sp_sealing_leght: Optional[float] = None
    sealing_sp_sealing_pressure: Optional[float] = None
    sealing_sp_sealing_wait_time: Optional[float] = None
    sealing_sp_sealing_wait_time_after_bars_return: Optional[float] = None
    vacuum_chamber_sp_abs_pressure_atm: Optional[float] = None
    vacuum_chamber_sp_atmospheric_pressure: Optional[float] = None
    vacuum_chamber_sp_atmospheric_pressure_up: Optional[float] = None
    vacuum_chamber_sp_atmospheric_pressure_down: Optional[float] = None
    vacuum_chamber_sp_delta_hysteresis_atm_pressure: Optional[float] = None
    vacuum_chamber_sp_sp_man_pressure: Optional[float] = None
    purging_db_high_pressure_sp: Optional[float] = None
    purging_db_low_pressure_sp: Optional[float] = None
    vacuum_chamber_sp_sp_min_pressure_tollerance: Optional[float] = None
    vacuum_chamber_sp_sp_pressure_range: Optional[float] = None
    safety_plc_oxigen_concentration: Optional[float] = None

"""
Filling
"""

@dataclass
class EFMFillingTimeSeries(Schema):
    __table_name__ = 'efm_filling_timeseries'
    __time_series__ = True

    timestamp: datetime
    filling_running: Optional[bool] = None
    actual_dosage: Optional[float] = None
    filling_flow: Optional[float] = None
    dosing_system_db_in_density: Optional[float] = None
    hmi_db_dosing_time: Optional[float] = None

@dataclass
class EFMFillingStatic(Schema):
    __table_name__ = 'efm_filling_static'
    __time_series__ = False

    timestamp: datetime
    main_enables_filling: Optional[bool] = None
    filling_enables_filling: Optional[bool] = None
    filling_enables_dosing_vaccum_step_1: Optional[bool] = None
    filling_enables_dosing_vaccum_step_2: Optional[bool] = None
    filling_enables_dosing_vaccum_step_3: Optional[bool] = None
    filling_enables_dosing_vaccum_step_4: Optional[bool] = None
    filling_enables_dosing_vaccum_step_5: Optional[bool] = None
    tank_electrolyte_qty_electrolyte_in_tank: Optional[float] = None
    tank_capacity_in_manual: Optional[float] = None
#   __percentage_slowdowns_dosing: Optional[float] = None
    dosing_controller_total_filling: Optional[float] = None

"""
Degassing
"""

@dataclass
class EFMDegassingTimeSeries(Schema):
    __table_name__ = 'efm_degassing_timeseries'
    __time_series__ = True

    timestamp: datetime
    degassing_running: Optional[bool] = None

@dataclass
class EFMDegassingStatic(Schema):
    __table_name__ = 'efm_degassing_static'
    __time_series__ = False

    timestamp: datetime
    main_enables_degassing: Optional[bool] = None
    degassing_enables_vacuum: Optional[bool] = None
    degassing_sp_sp_vaccumization: Optional[float] = None
    degassing_sp_sp_vaccum: Optional[float] = None
    degassing_enables_needles: Optional[bool] = None
    degassing_sp_sp_time_after_degassing: Optional[float] = None
    degassing_enables_sealingbars: Optional[bool] = None
    sealing_sp_sealing_wait_time_for_degassing: Optional[float] = None
    sealing_sp_sealing_wait_time_after_bars_return_for_degassing: Optional[float] = None
    inertizzation_db_high_pressure_sp: Optional[float] = None
    inertizzation_db_low_pressure_sp: Optional[float] = None
    inertizzation_db_high_pressure_reached: Optional[bool] = None
    inertizzation_db_low_pressure_reached: Optional[bool] = None


