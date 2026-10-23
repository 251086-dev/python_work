# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

# Runtime error: input() gives text, and Python cannot compare text with a number
# Old line: port = input("Port: ")
port = int(input("Port: "))

# Semantic error: = puts a value in a variable, but I want to compare, so I need ==
# Old line: is_admin = role = "admin"
is_admin = role == "admin"

# Syntax error: there is no operator called =<, the right one is <=
# Old line: is_system_port = port =< 1023
is_system_port = port <= 1023

# Semantic error: "or 443" alone is always True, I need to compare port with 443 too
# Old line: is_web_port = port == 80 or 443
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")