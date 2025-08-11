class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0
    def deposit(self, amount):
        amount += self.account_balance
        self.account_balance = amount
        return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")

        else:
            self.account_balance -= amount
            print('Withdrew: ${amount:.1f}')
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

        

