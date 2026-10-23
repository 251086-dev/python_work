# conditional_tests.py
# Ten conditional tests with my predictions

user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

print("\nIs port != 22? I predict False.")
print(port != 22)

print("\nIs failed > 3? I predict False.")
print(failed > 3)

print("\nIs port < 100? I predict True.")
print(port < 100)

print("\nIs failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs failed <= 2? I predict False.")
print(failed <= 2)

print("\nIs user == 'analyst' and role == 'viewer'? I predict True.")
print(user == "analyst" and role == "viewer")

print("\nIs role == 'admin' or port == 22? I predict True.")
print(role == "admin" or port == 22)

print("\nIs not failed == 3? I predict False.")
print(not failed == 3)