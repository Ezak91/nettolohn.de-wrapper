from enum import Enum


class UnemploymentInsurance(Enum):
    NOT_INSURED_BY_LAW = "nicht gesetzlich pflichtversichert"
    INSURED_BY_LAW = "gesetzlich pflichtversichert"
    ONLY_COMPULSORY_EMPLOYER_SHARE = "nur Arbeitgeber-Pflichtanteil"
    ONLY_COMPULSORY_EMPLOYEE_SHARE = "nur Arbeitnehmer-Pflichtanteil"
