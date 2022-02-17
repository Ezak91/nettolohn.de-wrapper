from enum import Enum


class Age(Enum):
    AGE_17 = "17 Jahre"
    AGE_18 = "18 Jahre"
    AGE_19 = "19 Jahre"
    AGE_20 = "20 Jahre"
    AGE_21 = "21 Jahre"
    AGE_22 = "22 Jahre"
    AGE_23 = "23 Jahre"
    AGE_24 = "24 Jahre"
    AGE_25 = "25 Jahre"
    AGE_26 = "26 Jahre"
    AGE_27 = "27 Jahre"
    AGE_28 = "28 Jahre"
    AGE_29 = "29 Jahre"
    AGE_30 = "30 Jahre"
    AGE_31 = "31 Jahre"
    AGE_32 = "32 Jahre"
    AGE_33 = "33 Jahre"
    AGE_34 = "34 Jahre"
    AGE_35 = "35 Jahre"
    AGE_36 = "36 Jahre"
    AGE_37 = "37 Jahre"
    AGE_38 = "38 Jahre"
    AGE_39 = "39 Jahre"
    AGE_40 = "40 Jahre"
    AGE_41 = "41 Jahre"
    AGE_42 = "42 Jahre"
    AGE_43 = "43 Jahre"
    AGE_44 = "44 Jahre"
    AGE_45 = "45 Jahre"
    AGE_46 = "46 Jahre"
    AGE_47 = "47 Jahre"
    AGE_48 = "48 Jahre"
    AGE_49 = "49 Jahre"
    AGE_50 = "50 Jahre"
    AGE_51 = "51 Jahre"
    AGE_52 = "52 Jahre"
    AGE_53 = "53 Jahre"
    AGE_54 = "54 Jahre"
    AGE_55 = "55 Jahre"
    AGE_56 = "56 Jahre"
    AGE_57 = "57 Jahre"
    AGE_58 = "58 Jahre"
    AGE_59 = "59 Jahre"
    AGE_60 = "60 Jahre"
    AGE_61 = "61 Jahre"
    AGE_62 = "62 Jahre"
    AGE_63 = "63 Jahre"
    AGE_64 = "64 Jahre"
    AGE_65 = "65 Jahre"
    AGE_66 = "66 Jahre"
    AGE_67 = "67 Jahre"
    AGE_68 = "68 Jahre"
    AGE_69 = "69 Jahre"
    AGE_70 = "70 Jahre"
    AGE_71 = "71 Jahre"
    AGE_72 = "72 Jahre"
    AGE_73 = "73 Jahre"
    AGE_74 = "74 Jahre"
    AGE_75 = "75 Jahre"
    AGE_76 = "76 Jahre"
    AGE_77 = "77 Jahre"


def get_enum_by_age(age: int) -> Age:
    """get age enum by age

    Args:
        age (int): the age as integer

    Returns:
        Age: the enum for the age
    """
    enum_name = "AGE_" + str(age)
    return Age.valueOf(enum_name)
