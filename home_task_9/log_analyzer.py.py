# log_analyzer.py
ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name):
    """Return the value after name=, up to the next space or the end."""
    start = line.find(name + "=")
    if start == -1:
        return ""
    start += len(name) + 1
    end = line.find(" ", start)
    if end == -1:
        return line[start:]
    return line[start:end]


def get_status(line):
    """Return the second word of the line: OK or FAILED."""
    parts = line.split()
    return parts[1]


def count_status(status):
    """Return how many lines of LOG have this status."""
    count = 0
    for line in LOG.splitlines():
        if get_status(line) == status:
            count += 1
    return count


def show_summary():
    """Display total lines and counts of FAILED and OK entries."""
    lines = LOG.splitlines()
    print(f"Lines: {len(lines)}")
    print(f"Failed: {count_status('FAILED')}")
    print(f"OK: {count_status('OK')}")


def search(keyword):
    """Display matching lines with line numbers (case-insensitive) and count."""
    needle = keyword.lower()
    matches = 0
    line_num = 1
    for line in LOG.splitlines():
        if needle in line.lower():
            print(f"{line_num}: {line}")
            matches += 1
        line_num += 1
    print(f"Matches: {matches}")


def ip_report(ip):
    """Display failed logins from ip, total count, and an alert if needed."""
    failures = 0
    for line in LOG.splitlines():
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            time_str = line[0:5]
            user_str = get_field(line, "user")
            print(f"{time_str} {user_str}")
            failures += 1
    print(f"Failed logins from {ip}: {failures}")
    if failures >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")


def mask(word):
    """Return first and last letters with * between them, or * for <= 2 chars."""
    if len(word) <= 2:
        return "*" * len(word)
    stars = "*" * (len(word) - 2)
    return word[0] + stars + word[-1]


def show_masked():
    """Display the entire LOG with every username masked."""
    for line in LOG.splitlines():
        user = get_field(line, "user")
        if user != "":
            masked_line = line.replace("user=" + user, "user=" + mask(user), 1)
        else:
            masked_line = line
        print(masked_line)


def show_menu():
    """Display the analyzer title and menu options."""
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")


show_menu()
while True:
    choice = input("Choice: ").strip().lower()
    if choice == "1":
        show_summary()
    elif choice == "2":
        kw = input("Keyword: ")
        search(kw)
    elif choice == "3":
        target_ip = input("IP: ")
        ip_report(target_ip)
    elif choice == "4":
        show_masked()
    elif choice == "q":
        print("Bye.")
        break
    else:
        print("Unknown choice.")