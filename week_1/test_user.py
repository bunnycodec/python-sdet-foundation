from user import Profile, User, AdminUser

profile = Profile("Bunny Singh", 28)
user = User("bunny", "bunny@test.com", True, profile)
assert user.is_active() is True
assert user.get_display_name() == "bunny (bunny@test.com)"
assert user.get_profile_summary() == "Bunny Singh | Age: 28"

user.deactivate()
assert user.is_active() is False

admin = AdminUser("root", "root@test.com", True, profile)
assert admin.is_admin() is True
assert admin.is_active() is True

admin.role = "viewer"
assert admin.is_active() is False
