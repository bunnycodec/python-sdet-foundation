class Validator:
    @staticmethod
    def withdrawal_permission(amount: float, balance: float):
        if amount > balance:
            raise ValueError("You do not have sufficient balance!")

    @staticmethod
    def amount_check(amount: float):
        if amount <= 0:
            raise ValueError("Invalid Amount!")
        
    @staticmethod
    def withdrawal_limit(amount: float):
        if amount > 5000:
            raise ValueError("You are not allowed to withdraw more than 5000!")
    
    @staticmethod
    def age_validator(age: int):
        if age < 18:
            raise ValueError("You are too young for opening a bank account!")
        
