from decimal import Decimal

from nettolohnde.enum.age import Age
from nettolohnde.enum.billing_period import BillingPeriod
from nettolohnde.enum.child_allowance import ChildAllowance
from nettolohnde.enum.health_insurance import HealthInsurance
from nettolohnde.enum.pension_insurance import PensionInsurance
from nettolohnde.enum.state import State
from nettolohnde.enum.tax_class import TaxClass


class SalaryCalculationInfos:

    # default constructor
    def __init__(
        self,
        gross_wage: Decimal,
        billing_period: BillingPeriod,
        company_pension_plan_month: Decimal,
        pecuniary_advantage: Decimal,
        accounting_year: int,
        tax_allowance_per_year: Decimal,
        tax_class: TaxClass,
        church_tax: bool,
        state: State,
        health_insurance: HealthInsurance,
        have_children: bool,
        age: Age,
        pension_insurance: PensionInsurance,
        tax_factor: Decimal = None,
        monthly_premium_phi: Decimal = None,
        employer_participation_phi: bool = None,
        health_insurance_rate: Decimal = None,
        child_allowance: ChildAllowance = None,
    ):
        self.gross_wage = gross_wage
        self.billing_period = billing_period
        self.company_pension_plan_month = company_pension_plan_month
        self.precuniary_advantage = pecuniary_advantage
        self.accounting_year = accounting_year
        self.tax_allowance_per_year = tax_allowance_per_year
        self.tax_class = tax_class
        self.church_tax = church_tax
        self.state = state
        self.health_insurance = health_insurance
        self.have_children = have_children
        self.age = age
        self.pension_insurance = pension_insurance
        self.tax_factor = tax_factor
        self.monthly_premium_phi = monthly_premium_phi
        self.employer_participation_phi = employer_participation_phi
        self.health_insurance_rate = health_insurance_rate
        self.child_allowance = child_allowance
