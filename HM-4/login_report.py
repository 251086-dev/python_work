MAX_LOGIN_ATTEMPTS = 5
user_name = input("Enter your name: ")
failed_number = int(input("Enter your failed number: "))

attempt_left = MAX_LOGIN_ATTEMPTS - failed_number 

equal = ("=" * 30)
title = "LOGIN REPORT"

print(equal)
print(title)
print(equal)
print(f"user_name:\t{user_name}")
print(f"failed_number:\t{failed_number}")
print(f"attempt_left:\t{attempt_left}")