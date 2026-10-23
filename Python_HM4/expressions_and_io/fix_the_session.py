# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")

# Runtime error: input() gives text, and Python cannot divide text, so I used int()
total_seconds = int(input("Session length in seconds: "))

# Semantic error: / gives 15.083..., I want whole minutes, so I need //
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)

# Semantic error: without the f, the braces are printed as plain text
print(f"User: {username}")

# Runtime error: I cannot add a number to text with +, so I used str(minutes)
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)