# username_policy.py
MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return username stripped of spaces and in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character not allowed in a username, or ""."""
    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            return ch
    return ""


def policy_problem(username):
    """Return the first username policy problem, or an empty string."""
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        return f"length must be {MIN_LENGTH} to {MAX_LENGTH}."
    if not username[0].isalpha():
        return "it must start with a letter."
    bad_ch = bad_character(username)
    if bad_ch != "":
        return f"the character {bad_ch} is not allowed."
    return ""


raw_name = input("New username: ")
cleaned_name = clean(raw_name)
problem = policy_problem(cleaned_name)

if problem == "":
    print(f"Accepted [{cleaned_name}].")
else:
    print(f"Rejected [{cleaned_name}]: {problem}")