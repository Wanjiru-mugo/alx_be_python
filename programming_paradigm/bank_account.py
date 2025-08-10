class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0
    def deposit(self, amount):
        amount += self.account_balance
        self.account_balance = amount
        return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if not amount > self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print('Insufficient funds')
            return False
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

        

