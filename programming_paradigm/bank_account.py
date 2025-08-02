class BankAccount:
    """account balance"""
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    """amount added to account balance"""
    def deposit(self, amount: float):
        self.account_balance += amount
    """amount removed to account balance"""
    def withdraw(self, amount: float):
        self.account_balance -= amount
    """displays the account balance after removing and adding amounts"""
    def display_balance(self):
        print("Your balance is:", self.account_balance)

account = BankAccount()

depo = float(input("Deposited: "))
draw = float(input("Withdraw: "))
account.deposit(depo)
account.withdraw(draw)

account.display_balance()

