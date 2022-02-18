from enum import Enum


class SalariesPerYear(Enum):
    SALARIES_12 = 12
    SALARIES_13 = 13
    SALARIES_14 = 14


def get_enum_by_salaries_number(salaries_number: int) -> SalariesPerYear:
    """get enum by salaries_number

    Args:
        salaries_number (int): the number of salaries

    Returns:
        SalariesPerYear: The enum
    """
    enum_name = "SALARIES_" + str(salaries_number)
    return SalariesPerYear.valueOf(enum_name)
