# fix_the_alert.py
# This program prints a five-line login alert.

print("=== LOGIN ALERT ===")

# Syntax error: there was a space at the start of the line
print("A new device signed in to your account.")

# Runtime error: Print with a capital P is not defined, it must be print
print("Time: 09:15")

# Syntax error: the closing quote was missing
print("If this was not you, change your password.")

# Syntax error: the closing parenthesis was missing
print("Contact the IT team for help.")

# Python reads the whole file first, so it reports syntax errors before running anything.
# The runtime error shows only when Python reaches that line.