
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from digital_dryroom.schema.schema import Schema

@dataclass
class ZFSTimeSeries(Schema):
    __table_name__ = 'zfs_timeseries'
    __time_series__ = True

    timestamp: datetime
    auto_start: Optional[bool] = None
    lc_act_photoid_0_last_electrode: Optional[float] = None
    lc_act_rot_0_last_electrode: Optional[float] = None
    lc_act_x_0_last_electrode: Optional[float] = None
    lc_act_y_0_last_electrode: Optional[float] = None
    lc_act_photoid_1_electrode: Optional[float] = None
    lc_act_rot_1_electrode: Optional[float] = None
    lc_act_x_1_electrode: Optional[float] = None
    lc_act_y_1_electrode: Optional[float] = None
    lc_act_photoid_2_electrode: Optional[float] = None
    lc_act_rot_2_electrode: Optional[float] = None
    lc_act_x_2_electrode: Optional[float] = None
    lc_act_y_2_electrode: Optional[float] = None
    lc_act_photoid_3_electrode: Optional[float] = None
    lc_act_rot_3_electrode: Optional[float] = None
    lc_act_x_3_electrode: Optional[float] = None
    lc_act_y_3_electrode: Optional[float] = None
    lc_act_photoid_4_electrode: Optional[float] = None
    lc_act_rot_4_electrode: Optional[float] = None
    lc_act_x_4_electrode: Optional[float] = None
    lc_act_y_4_electrode: Optional[float] = None
    lc_act_photoid_5_electrode: Optional[float] = None
    lc_act_rot_5_electrode: Optional[float] = None
    lc_act_x_5_electrode: Optional[float] = None
    lc_act_y_5_electrode: Optional[float] = None
    lc_act_photoid_6_electrode: Optional[float] = None
    lc_act_rot_6_electrode: Optional[float] = None
    lc_act_x_6_electrode: Optional[float] = None
    lc_act_y_6_electrode: Optional[float] = None
    lc_act_photoid_7_electrode: Optional[float] = None
    lc_act_rot_7_electrode: Optional[float] = None
    lc_act_x_7_electrode: Optional[float] = None
    lc_act_y_7_electrode: Optional[float] = None
    lc_act_photoid_8_electrode: Optional[float] = None
    lc_act_rot_8_electrode: Optional[float] = None
    lc_act_x_8_electrode: Optional[float] = None
    lc_act_y_8_electrode: Optional[float] = None
    lc_act_photoid_9_electrode: Optional[float] = None
    lc_act_rot_9_electrode: Optional[float] = None
    lc_act_x_9_electrode: Optional[float] = None
    lc_act_y_9_electrode: Optional[float] = None
    lc_act_photoid_10_electrode: Optional[float] = None
    lc_act_rot_10_electrode: Optional[float] = None
    lc_act_x_10_electrode: Optional[float] = None
    lc_act_y_10_electrode: Optional[float] = None
    lc_act_photoid_11_electrode: Optional[float] = None
    lc_act_rot_11_electrode: Optional[float] = None
    lc_act_x_11_electrode: Optional[float] = None
    lc_act_y_11_electrode: Optional[float] = None
    lc_act_photoid_12_electrode: Optional[float] = None
    lc_act_rot_12_electrode: Optional[float] = None
    lc_act_x_12_electrode: Optional[float] = None
    lc_act_y_12_electrode: Optional[float] = None
    lc_act_photoid_13_electrode: Optional[float] = None
    lc_act_rot_13_electrode: Optional[float] = None
    lc_act_x_13_electrode: Optional[float] = None
    lc_act_y_13_electrode: Optional[float] = None
    lc_act_photoid_14_electrode: Optional[float] = None
    lc_act_rot_14_electrode: Optional[float] = None
    lc_act_x_14_electrode: Optional[float] = None
    lc_act_y_14_electrode: Optional[float] = None
    lc_act_photoid_15_electrode: Optional[float] = None
    lc_act_rot_15_electrode: Optional[float] = None
    lc_act_x_15_electrode: Optional[float] = None
    lc_act_y_15_electrode: Optional[float] = None
    rc_act_photoid_0_last_electrode: Optional[float] = None
    rc_act_rot_0_last_electrode: Optional[float] = None
    rc_act_x_0_last_electrode: Optional[float] = None
    rc_act_y_0_last_electrode: Optional[float] = None
    rc_act_photoid_1_electrode: Optional[float] = None
    rc_act_rot_1_electrode: Optional[float] = None
    rc_act_x_1_electrode: Optional[float] = None
    rc_act_y_1_electrode: Optional[float] = None
    rc_act_photoid_2_electrode: Optional[float] = None
    rc_act_rot_2_electrode: Optional[float] = None
    rc_act_x_2_electrode: Optional[float] = None
    rc_act_y_2_electrode: Optional[float] = None
    rc_act_photoid_3_electrode: Optional[float] = None
    rc_act_rot_3_electrode: Optional[float] = None
    rc_act_x_3_electrode: Optional[float] = None
    rc_act_y_3_electrode: Optional[float] = None
    rc_act_photoid_4_electrode: Optional[float] = None
    rc_act_rot_4_electrode: Optional[float] = None
    rc_act_x_4_electrode: Optional[float] = None
    rc_act_y_4_electrode: Optional[float] = None
    rc_act_photoid_5_electrode: Optional[float] = None
    rc_act_rot_5_electrode: Optional[float] = None
    rc_act_x_5_electrode: Optional[float] = None
    rc_act_y_5_electrode: Optional[float] = None
    rc_act_photoid_6_electrode: Optional[float] = None
    rc_act_rot_6_electrode: Optional[float] = None
    rc_act_x_6_electrode: Optional[float] = None
    rc_act_y_6_electrode: Optional[float] = None
    rc_act_photoid_7_electrode: Optional[float] = None
    rc_act_rot_7_electrode: Optional[float] = None
    rc_act_x_7_electrode: Optional[float] = None
    rc_act_y_7_electrode: Optional[float] = None
    rc_act_photoid_8_electrode: Optional[float] = None
    rc_act_rot_8_electrode: Optional[float] = None
    rc_act_x_8_electrode: Optional[float] = None
    rc_act_y_8_electrode: Optional[float] = None
    rc_act_photoid_9_electrode: Optional[float] = None
    rc_act_rot_9_electrode: Optional[float] = None
    rc_act_x_9_electrode: Optional[float] = None
    rc_act_y_9_electrode: Optional[float] = None
    rc_act_photoid_10_electrode: Optional[float] = None
    rc_act_rot_10_electrode: Optional[float] = None
    rc_act_x_10_electrode: Optional[float] = None
    rc_act_y_10_electrode: Optional[float] = None
    rc_act_photoid_11_electrode: Optional[float] = None
    rc_act_rot_11_electrode: Optional[float] = None
    rc_act_x_11_electrode: Optional[float] = None
    rc_act_y_11_electrode: Optional[float] = None
    rc_act_photoid_12_electrode: Optional[float] = None
    rc_act_rot_12_electrode: Optional[float] = None
    rc_act_x_12_electrode: Optional[float] = None
    rc_act_y_12_electrode: Optional[float] = None
    rc_act_photoid_13_electrode: Optional[float] = None
    rc_act_rot_13_electrode: Optional[float] = None
    rc_act_x_13_electrode: Optional[float] = None
    rc_act_y_13_electrode: Optional[float] = None
    rc_act_photoid_14_electrode: Optional[float] = None
    rc_act_rot_14_electrode: Optional[float] = None
    rc_act_x_14_electrode: Optional[float] = None
    rc_act_y_14_electrode: Optional[float] = None
    rc_act_photoid_15_electrode: Optional[float] = None
    rc_act_rot_15_electrode: Optional[float] = None
    rc_act_x_15_electrode: Optional[float] = None
    rc_act_y_15_electrode: Optional[float] = None




@dataclass
class ZFSStatic(Schema):
    __table_name__ = 'zfs_static'
    __time_series__ = False

    timestamp: datetime
    unw_high_tension: Optional[float] = None
    gen_anode_thickness: Optional[float] = None
    gen_anode_length: Optional[float] = None
    gen_anode_width: Optional[float] = None
    gen_num_anode: Optional[float] = None
    gen_cathode_thickness: Optional[float] = None
    gen_cathode_length: Optional[float] = None
    gen_cathode_width: Optional[float] = None
    gen_num_cathode: Optional[float] = None
    gen_separator_thickness: Optional[float] = None
    gen_separator_length: Optional[float] = None
    gen_separator_width: Optional[float] = None
    cell_stack_height: Optional[float] = None
    total_cells_after_startup: Optional[float] = None
    lc_sp_rot: Optional[float] = None
    lc_sp_x: Optional[float] = None
    lc_sp_y: Optional[float] = None
    rc_sp_rot: Optional[float] = None
    rc_sp_x: Optional[float] = None
    rc_sp_y: Optional[float] = None

