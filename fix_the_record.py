# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router"

# Syntax Error: Variable name cannot start with a number
second_ip = "192.0.2.1"

# Syntax Error: class is a reserved word in Python
device_class = "router"

# Runtime Error: Cannot turn "twenty-two" into a number
port = 22

# Syntax Error: Variable name was spelled wrong (device_nam)
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)

# Explanation:
# Python finds syntax errors first before running the code.
# Runtime errors happen later when the code actually runs.