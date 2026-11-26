# ip_check.py


def is_valid_part(part):
    """Return True if part has only digits and is between 0 and 255."""
    if not part.isdecimal():
        return False
    return int(part) <= 255


def ip_problem(address):
    """Return the first IPv4 validation problem, or an empty string."""
    if address.count(".") != 3:
        return "it needs exactly 3 dots."

    parts = address.split(".")
    for part in parts:
        if part == "":
            return "a part is empty."
        if not is_valid_part(part):
            return f"{part} is not a number from 0 to 255."

    return ""


raw_address = input("IPv4 address: ")
cleaned_address = raw_address.strip()
problem = ip_problem(cleaned_address)

if problem == "":
    print(f"{cleaned_address} is valid.")
else:
    print(f"Invalid: {problem}")