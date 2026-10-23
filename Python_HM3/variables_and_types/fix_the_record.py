# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router"

# Syntax Error: a variable name cannot start with a number
second_ip = "192.0.2.1"

# Syntax Error: class is a reserved word in Python
device_class = "router"

# Runtime Error: Python cannot turn "twenty-two" into a number
port = 22

# Runtime Error: the name device_nam does not exist (NameError), the right name is device_name
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)

# Explanation:
# Python reads the whole file first, so it finds syntax errors before running anything.
# Runtime errors happen later, only when Python reaches that line.