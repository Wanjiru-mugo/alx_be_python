class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def deposit(self, amount):
        amount += self.account_balance
        self.account_balance = amount
        self.initial_balance = 0
        return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False

        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

        

