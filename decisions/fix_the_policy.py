# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# syntax: added the missing colon after the if condition
if len(password) < MIN_LENGTH:
    print("- Too short.")
# semantic: changed elif to if so both problems are reported
if password == username:
    print("- Same as the username.")

# semantic: the narrowest test (>= 16) must come first in the chain
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
# semantic: print was inside the else block; now it always runs
print(f"Length: {len(password)} ({strength})")