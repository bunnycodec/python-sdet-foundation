ui_tests = ["login", "signup", "logout", "profile"]
api_tests = ["login", "logout", "settings"]

ui_tests = set(ui_tests)
api_tests = set(api_tests)


result: dict[str, set[str]] = {
    "common": ui_tests & api_tests,
    "ui_only": ui_tests - api_tests,
    "api_only": api_tests - ui_tests
}

print(result)