class Profile:
    def __init__(self, full_name: str, age: int) -> None:
        self.full_name = full_name
        self.age = max(age, 0)

class User:
    def __init__(self, username: str, email: str, active: bool, profile: Profile) -> None:
        self.username = username
        self.email = email
        self.active = active
        self.profile = profile

    def is_active(self) -> bool:
        return self.active
    
    def deactivate(self) -> None:
        self.active = False

    def get_display_name(self) -> str:
        return f"{self.username} ({self.email})"
    
    def get_profile_summary(self) -> str:
        return f"{self.profile.full_name} | Age: {self.profile.age}"
    

class AdminUser(User):
    def __init__(self, username: str, email: str, active: bool, profile: Profile) -> None:
        super().__init__(username, email, active, profile)
        self.role = "admin"

    def is_active(self) -> bool:
        return super().is_active() and self.role == "admin"
    
    def is_admin(self) -> bool:
        return True
    

