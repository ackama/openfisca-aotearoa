"""TODO: Add missing doctring."""

import numpy

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class family_scheme__qualifies_for_in_work_tax_credit(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "Is a person is qualified as eligible for the in-work tax credit"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518522.html"

    def formula(persons, period, parameters):
        base_qualifies = persons("family_scheme__base_qualifies", period)
        received_tested_benefit = persons("social_security__received_income_tested_benefit", period.this_year)
        received_parents_allowance = persons("veterans_support__received_parents_allowance", period)
        received_childrens_pension = persons("veterans_support__received_childrens_pension", period)

        return base_qualifies * numpy.logical_not(received_tested_benefit) * numpy.logical_not(received_parents_allowance) \
            * numpy.logical_not(received_childrens_pension) * persons("family_scheme__in_work_tax_credit_income_under_threshold", period) \
            * persons("family_scheme__full_time_earner", period)


class family_scheme__in_work_tax_credit_income_under_threshold(variables.Variable):  # this variable is a proxy for the calculation "family_scheme__in_work_tax_credit_entitlement" which needs to be coded
    value_type = bool
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "Is the income under the threshold for the in work tax credit"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518484.html"


class family_scheme__in_work_tax_credit_entitlement(variables.Variable):
    value_type = float
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "The in-work tax credit entitlement a person has under the family scheme"
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518521.html"

    def formula(persons, period, parameters):
        # TODO
        return persons
