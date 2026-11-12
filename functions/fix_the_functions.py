# fix_the_functions.py


def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        # semantic: the function must return the total, not always 0
        return failed * minutes
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# runtime: print_header() was called before its def (NameError); call it after
print_header()
# runtime: user= is not a parameter name; the exact name is username= (TypeError)
print(login_line(username="sara", failed=4))
# semantic: the returned line was never displayed; wrap the call in print()
print(login_line("omar", 1))
