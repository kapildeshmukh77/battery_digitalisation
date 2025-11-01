from digital_dryroom.schema.bfm import BFMStatic, BFMTimeSeries
from digital_dryroom.schema.efm import (EFMFillingStatic, EFMFillingTimeSeries, EFMDegassingStatic, EFMGeneralStatic,
                                        EFMGeneralTimeSeries, EFMDegassingTimeSeries)
from digital_dryroom.schema.schema import Schema
from digital_dryroom.schema.zfs import ZFSTimeSeries, ZFSStatic

all_schemas = [BFMStatic, BFMTimeSeries, EFMFillingStatic, EFMFillingTimeSeries, EFMDegassingStatic, EFMGeneralStatic,
                                        EFMGeneralTimeSeries, EFMDegassingTimeSeries, ZFSTimeSeries, ZFSStatic]