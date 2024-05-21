class Person:
    def __init__(self, name):
        # Initialize person's name and common deductions.
        self.name = name
        self.general_deductions = {
            "education_allowance": 0,
            "life_insurance_premium": 0,
            "self_education_allowance": 0,
            "donations": 0,
            "sponsored_children_expense": 0
        }

    def calculate_tax(self, total_income):
        # Calculate tax payable based on income after deductions.

        # Calculate total deductions.
        total_deductions = sum(self.general_deductions.values())

        # Calculate taxable income after deducting total deductions.
        taxable_income = total_income - total_deductions

        # If the taxable income is less than or equal to Nu. 300,000,
        # exempt the individual from paying taxes and return 0.
        if taxable_income <= 300000:
            print(f"{self.name} is exempted from taxation as their income is less than Nu. 300,000.")
            return 0
        
        # Define tax brackets to determine tax rates based on income ranges.
        tax_brackets = [
            (300000, 0.0),  
            (400000, 0.1),  
            (650000, 0.15), 
            (1000000, 0.2), 
            (1500000, 0.25), 
            (float('inf'), 0.3)  
        ]

        # Calculate tax payable based on tax brackets.
        tax_payable = 0
        previous_limit = 0

        for limit, rate in tax_brackets:
            if taxable_income > limit:
                taxable_amount = limit - previous_limit
                tax_payable += taxable_amount * rate
                previous_limit = limit
            else:
                taxable_amount = taxable_income - previous_limit
                tax_payable += taxable_amount * rate
                break

        # Apply additional tax for incomes >= 1000000.
        if tax_payable >= 1000000:
            tax_payable *= 1.1

        return tax_payable

    def calculate_income(self):
        pass  # Placeholder method to be overridden by subclasses

class Employee(Person):
    def __init__(self, name, employment_income, pf_contribution=0, gis_contribution=0, contract_employee=False):
        # Initialize employee's name, employment income, and contributions.
        super().__init__(name)
        self.employment_income = employment_income
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.contract_employee = contract_employee

    def calculate_income(self):
        # Calculate employee's net salary income after deducting contributions.
        if not self.contract_employee:
            salary_income = self.employment_income - self.pf_contribution - self.gis_contribution
        else:
            salary_income = self.employment_income
        return salary_income

class Landlord(Person):
    def __init__(self, name, rental_income, repairs_maintenance, interest_payments, urban_taxes, insurance_premium):
        # Initialize landlord's name and rental-related income and expenses.
        super().__init__(name)
        self.rental_income = rental_income
        self.repairs_maintenance = repairs_maintenance
        self.interest_payments = interest_payments
        self.urban_taxes = urban_taxes
        self.insurance_premium = insurance_premium

    def calculate_income(self):
        # Calculate landlord's net rental income after deducting expenses.
        taxable_rental_income = self.rental_income - (0.2 * (self.repairs_maintenance + self.interest_payments + self.urban_taxes + self.insurance_premium))
        return taxable_rental_income

class Investor(Person):
    def __init__(self, name, dividend_income, loan_interest):
        # Initialize investor's name and dividend and loan-related income.
        super().__init__(name)
        self.dividend_income = dividend_income
        self.loan_interest = loan_interest

    def calculate_income(self):
        # Calculate investor's net taxable dividend income after deductions.
        taxable_dividend_income = self.dividend_income - 30000 - self.loan_interest
        return taxable_dividend_income if taxable_dividend_income > 0 else 0

class Consultant(Person):
    def __init__(self, name, other_income):
        # Initialize consultant's name and other sources of income.
        super().__init__(name)
        self.other_income = other_income

    def calculate_income(self):
        # Calculate consultant's net taxable income from other sources.
        taxable_other_income = 0.7 * self.other_income
        return taxable_other_income if taxable_other_income > 0 else 0

class Organisation:
    def __init__(self, name, sector):
        # Initialize organisation's name and sector.
        self.name = name
        self.sector = sector

class Government(Organisation):
    def __init__(self, name):
        # Initialize government organisation with its name.
        super().__init__(name, "Government")

class Private(Organisation):
    def __init__(self, name):
        # Initialize private organisation with its name.
        super().__init__(name, "Private")

class Corporate(Organisation):
    def __init__(self, name):
        # Initialize corporate organisation with its name.
        super().__init__(name, "Corporate")

# Objects or Test Classes
employee = Employee("Karma Wangdi", 320000, 20000, 5000)
landlord = Landlord("Karma Rangdrel", 340000, 15000, 2000, 3000, 5000)
investor = Investor("Jatsho", 310000, 5000)
consultant = Consultant("Pelden Wangchuk", 330000)
government = Government("Bhutan Telecome")
private_company = Private("Tashi Company")
corporate_company = Corporate("Bhutan Power Corporation Limited")

# Output the organisation each person works for
print(f"{employee.name} is exempted from tax and works at {private_company.name} ({private_company.sector} Sector)")
print(f"{landlord.name} works at {private_company.name} ({private_company.sector} Sector)")
print(f"{investor.name} works at {corporate_company.name} ({corporate_company.sector} Sector)")
print(f"{consultant.name} works at {private_company.name} ({private_company.sector} Sector)")

# Output the income and tax details for each person
for person in [employee, landlord, investor, consultant]:
    income = person.calculate_income()
    tax = person.calculate_tax(income)
    print(f"{person.name}'s total income: Nu. {income:.2f}")
    print(f"{person.name}'s total tax payable: Nu. {tax:.2f}")
