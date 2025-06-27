class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, base_salary, bonus, stock_options):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.stock_options = stock_options

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.stock_options

# Example usage
employees = [
    RegularEmployee("Meena", 50000, 5000),
    ContractEmployee("Maha", 100, 160),
    Manager("Vishnu", 80000, 10000, 15000)
]

for emp in employees:
    print(f"{emp.name}'s salary: ${emp.calculate_salary():,.2f}")
