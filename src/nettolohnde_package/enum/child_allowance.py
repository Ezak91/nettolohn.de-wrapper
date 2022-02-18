from enum import Enum
from decimal import Decimal


class ChildAllowance(Enum):
    Allowance0 = 0
    Allowance0_5 = 0.5
    Allowance1 = 1
    Allowance1_5 = 1.5
    Allowance2 = 2
    Allowance2_5 = 2.5
    Allowance3 = 3
    Allowance3_5 = 3.5
    Allowance4 = 4
    Allowance4_5 = 4.5
    Allowance5 = 5
    Allowance5_5 = 5.5
    Allowance6 = 6


def get_enum_by_value(value: Decimal) -> ChildAllowance:
    """get enum by decimal value

    Args:
        value (Decimal): the decimal value

    Returns:
        ChildAllowance: The enum
    """
    value_dot = str(value)
    value_underscore = value_dot.replace(".", "_")
    enum_name = "Allowance" + value_underscore
    return ChildAllowance.valueOf(enum_name)
