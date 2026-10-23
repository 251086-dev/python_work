# login_report.py
# This program prints a login report for a user.

MAX_LOGIN_ATTEMPTS = 5

user_name = input("Username: ")
failed_number = int(input("Failed attempts: "))

attempt_left = MAX_LOGIN_ATTEMPTS - failed_number

equal = "=" * 30
title = "LOGIN REPORT"

print(equal)
print(title)
print(equal)
print(f"User:\t\t{user_name}")
print(f"Failed:\t\t{failed_number}")
print(f"Attempts left:\t{attempt_left}")