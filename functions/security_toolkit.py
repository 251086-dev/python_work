# security_toolkit.py
# A small menu program with nine functions, one job each.
MIN_LENGTH = 8


def border(width):
    """Display a box border for text of the given width."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Display text inside a box."""
    border(len(text))
    print(f"| {text} |")
    border(len(text))


def show_menu():
    """Display the title and the menu lines."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return invalid, system, user, or dynamic for a port number."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    return "dynamic"


def check_port():
    """Ask for a port and show its range in a box."""
    port = int(input("Port: "))
    show_box(f"Port {port}: {port_range(port)}")


def password_problem(password, username):
    """Return the first problem with the password, or an empty string."""
    if len(password) < MIN_LENGTH:
        return "too short"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask for a username and password and show the result in a box."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Return the whole days needed to try every PIN."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask for PIN digits and a guess rate, then show the days in a box."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    show_box(f"{digits} digits: {days_to_guess(digits, per_second)} days")


show_menu()
checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        break
    else:
        print("Unknown choice.")

show_box(f"Checks done: {checks}")
