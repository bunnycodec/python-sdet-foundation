from src.account import Account
from src.validators import Validator

class Services:
    def create_account(self, name: str, age: int) -> Account:
        validator = Validator()
        validator.age_validator(age)
        return Account(1, name, age)

    def withdrawal(self, account: Account, amount: float):
        validator = Validator()
        validator.amount_check(amount)
        validator.withdrawal_limit(amount)
        validator.withdrawal_permission(amount, account.balance)
        account.balance -= amount
        account.transactions.append({"Type": "Withdrawal", "Amount": amount, "Current_Balance": account.balance})

    def deposit(self, account: Account, amount: int):
        validator = Validator()
        validator.amount_check(amount)
        account.balance += amount
        account.transactions.append({"Type": "Deposit", "Amount": amount, "Current_Balance": account.balance})

    def get_balance(self, account: Account):
        return account.balance
    
    def get_transaction_list(self, account: Account):
        return account.transactions

