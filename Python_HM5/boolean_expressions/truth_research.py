# truth_research.py
# Which values count as True and which as False?

# Prediction: bool("") is False, because an empty string has nothing inside
print(bool(""))

# Prediction: bool("0") is True, because it is a string with a character inside
# (it is not the number zero)
print(bool("0"))

# Prediction: bool(0) is False, because the number zero counts as False
print(bool(0))

# Prediction: bool(0.0) is False, because zero as a float is also False
print(bool(0.0))

# Prediction: bool("False") is True, because it is a string that is not empty
# (Python does not read the word, it only sees that the string is not empty)
print(bool("False"))

# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing