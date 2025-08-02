class BankAccount:
    """account balance"""
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    """amount added to account balance"""
    def deposit(self, amount: float):
        self.account_balance += amount

    """amount removed to account balance"""
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False  # Withdrawal failed
        self.account_balance -= amount
        return True  # Withdrawal successful

    """displays the account balance after removing and adding amounts"""
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")