# int_research.py - Testing int() with different strings

# Predictions:
# " 22 " -> Works because spaces around numbers are ignored
# "+22"  -> Works because + sign is allowed
# "0022" -> Works because leading zeros are allowed
# "2_2"  -> Works because underscores are allowed in numbers

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))

# Documentation link:
# https://docs.python.org/3/library/functions.html#int