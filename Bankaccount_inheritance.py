class BankAccount:
    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self._balance = balance # encapsulated balance

    def deposit(self,amount):
        self._balance += amount
        print(f"Deposited {amount}.New balance:{self._balance}")

    def withdraw(self,amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance-= amount
        return f"An account number {self.account_number} has withdrawn an amount {amount} and the balance is {self._balance}"

    def get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):  # Protected setter
        self.__balance = new_balance

class Savingsaccount(BankAccount):
# calculate interest rate and method to calculate interest
    def __init__(self,account_number,balance=0,interest_Rate=0.02):
        super().__init__(account_number, balance)
        self.interest_Rate = interest_Rate

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_Rate / 100)
        self.deposit(interest)
        print(f"Interest of {interest:.2f} applied at rate {self.interest_Rate}%.")

# Subclass: CurrentAccount with minimum balance requirement
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, minimum_balance=500.0):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if self.get_balance() - amount >= self.minimum_balance:
            self._set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print(f"Cannot withdraw {amount}. Minimum balance of {self.minimum_balance} must be maintained.")

obj1 = BankAccount(143333,600)
print(obj1.deposit(100))
print(obj1.withdraw(500))

