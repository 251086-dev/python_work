# password_check.py
# Accept a password only if it passes two checks.


def long_enough(password, minimum=8):
    """Return True if the password has at least minimum characters."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Return True if the password is not the same as the username."""
    return password != username


def password_ok(password, username):
    """Return True only if both checks pass."""
    return long_enough(password) and differs_from_username(password, username)


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")
