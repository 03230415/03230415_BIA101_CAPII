class Person:
    def __init__(self, name, salary, allowances=0):
        self.name = name
        self.salary = salary
        self.allowances = allowances

    def calculate_gross_income(self):
        return self.salary + self.allowances

    def calculate_tax(self):
        gross_income = self.calculate_gross_income()
        deductions = self.calculate_deductions()
        taxable_income = gross_income - deductions
        
        if taxable_income <= 300000:
            return 0
        elif taxable_income <= 400000:
            return (taxable_income - 300000) * 0.10
        elif taxable_income <= 650000:
            return 10000 + (taxable_income - 400000) * 0.15
        elif taxable_income <= 1000000:
            return 47500 + (taxable_income - 650000) * 0.20
        elif taxable_income < 1500000:
            return 117500 + (taxable_income - 1000000) * 0.25
        else:
            actual_tax = 242500 + (taxable_income - 1500000) * 0.30
            surcharge = actual_tax * 0.10 if actual_tax >= 100000 else 0
            return actual_tax + surcharge


class Employee(Person):
    def __init__(self, name, salary, allowances, pf=0, gis=0, children=0):
        super().__init__(name, salary, allowances)
        self.pf = pf
        self.gis = gis
        self.children = children

    def calculate_deductions(self):
        # Specific deductions for employees
        pf_deduction = self.pf
        gis_deduction = self.gis
        children_education_allowance = min(35000, self.children * 35000)
        return pf_deduction + gis_deduction + children_education_allowance


class RegularEmployee(Employee):
    def __init__(self, name, salary, allowances, pf, gis, children):
        super().__init__(name, salary, allowances, pf, gis, children)


class ContractEmployee(Employee):
    def __init__(self, name, salary, allowances, children):
        # Contract employees do not have pf/gis deduction
        super().__init__(name, salary, allowances, pf=0, gis=0, children=children)


class GovernmentEmployee(RegularEmployee):
    pass


class PrivateEmployee(RegularEmployee):
    pass


class CorporateEmployee(RegularEmployee):
    pass


# Example usage
if __name__ == "__main__":
    gov_employee = GovernmentEmployee("Pala", 500000, 15000, 35000, 11000, 2)
    private_employee = PrivateEmployee("Tagg", 1500000, 50000, 60000, 10000, 1)
    contract_employee = ContractEmployee("Bal", 450000, 45000, 2)

    print(f"{gov_employee.name}'s total tax payable: Nu. {gov_employee.calculate_tax():.2f}")
    print(f"{private_employee.name}'s total tax payable: Nu. {private_employee.calculate_tax():.2f}")
    print(f"{contract_employee.name}'s total tax payable: Nu. {contract_employee.calculate_tax():.2f}")
