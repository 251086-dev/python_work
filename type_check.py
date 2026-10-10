# type_check.py - Checking and converting data types

# Predictions:
# 8080 -> int
# "8080" -> str
# 99.5 -> float
# "198.51.100.7" -> str
# 1_000 -> int

# Print the type of each value
print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))

# Convert values
a = int("443")
b = str(8080)
c = float("2.5")

# Print converted values with their types
print(a, type(a))
print(b, type(b))
print(c, type(c))