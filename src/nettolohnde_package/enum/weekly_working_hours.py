from decimal import Decimal
from enum import Enum


class WeeklyWorkingHours(Enum):
    HOURS_15 = 15
    HOURS_15_5 = 15.5
    HOURS_16 = 16
    HOURS_16_5 = 16.5
    HOURS_17 = 17
    HOURS_17_5 = 17.5
    HOURS_18 = 18
    HOURS_18_5 = 18.5
    HOURS_19 = 19
    HOURS_19_5 = 19.5
    HOURS_20 = 20
    HOURS_20_5 = 20.5
    HOURS_21 = 21
    HOURS_21_5 = 21.5
    HOURS_22 = 22
    HOURS_22_5 = 22.5
    HOURS_23 = 23
    HOURS_23_5 = 23.5
    HOURS_24 = 24
    HOURS_24_5 = 24.5
    HOURS_25 = 25
    HOURS_25_5 = 25.5
    HOURS_26 = 26
    HOURS_26_5 = 26.5
    HOURS_27 = 27
    HOURS_27_5 = 27.5
    HOURS_28 = 28
    HOURS_28_5 = 28.5
    HOURS_29 = 29
    HOURS_29_5 = 29.05
    HOURS_30 = 30
    HOURS_30_5 = 30.5
    HOURS_31 = 31
    HOURS_31_5 = 31.5
    HOURS_32 = 32
    HOURS_32_5 = 32.5
    HOURS_33 = 33
    HOURS_33_5 = 33.5
    HOURS_34 = 34
    HOURS_34_5 = 34.5
    HOURS_35 = 35
    HOURS_35_5 = 35.5
    HOURS_36 = 36
    HOURS_36_5 = 36.5
    HOURS_37 = 37
    HOURS_37_5 = 37.5
    HOURS_38 = 38
    HOURS_38_5 = 38.5
    HOURS_39 = 39
    HOURS_39_5 = 39.5
    HOURS_40 = 40
    HOURS_40_5 = 40.5
    HOURS_41 = 41
    HOURS_41_5 = 41.5
    HOURS_42 = 42
    HOURS_42_5 = 42.5
    HOURS_43 = 43
    HOURS_43_5 = 43.5
    HOURS_44 = 44
    HOURS_44_5 = 44.5
    HOURS_45 = 45
    HOURS_45_5 = 45.5
    HOURS_46 = 46


def get_enum_by_hours(hours: Decimal) -> WeeklyWorkingHours:
    """get hours enum by hours

    Args:
        hours (Decimal): the hours as Decimal

    Returns:
        WeeklyWorkingHours: the enum for the hours
    """
    name_dot = str(hours)
    name_underscore = name_dot.replace(".", "_")
    enum_name = "HOURS_" + name_underscore
    return WeeklyWorkingHours.valueOf(enum_name)
