# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: slice end index is exclusive, so 0:5 returns 5 characters
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: lower() returns a new string; return its result
    return user.lower()


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: "in" is case-sensitive; compare lowercase to match "FAILED"
    return "failed" in line.lower()


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings are immutable and do not support item assignment
    return "*" + user[1:]


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime: len is a built-in function, not a method on str
print(f"Length: {len(LINE)}")