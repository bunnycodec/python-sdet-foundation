class User:
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name = name
        self.email = email
        self.age = age


class UserValidator:
    @staticmethod
    def validate_name(name: str):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty or whitespace.")

    @staticmethod   
    def validate_age(age: int):
        if age < 18:
            raise ValueError("Age cannot be less than 18 years old.")
    
    @staticmethod
    def validate_email(email: str):
        if email.count("@") != 1:
            raise ValueError("Email must contain exactly one @.")

        if "." not in email.split("@")[1]:
            raise ValueError("Email domain must contain a dot.")


class UserService:
    def register_user(self, name: str, email: str, age: int) -> User:
        UserValidator.validate_name(name)
        UserValidator.validate_age(age)
        UserValidator.validate_email(email)

        return User(name, email, age)
