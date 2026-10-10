# device_card.py - A program to store device details

# One constant
MAX_CONNECTIONS = 100

# Four variables
device_name = "web-server-01"
device_ip = "192.0.2.20"
service = "HTTPS"
open_port = 443

# Print each value with a label
print("Device:", device_name)
print("IP address:", device_ip)
print("Service:", service)
print("Port:", open_port)
print("Max connections:", MAX_CONNECTIONS)

# Change two values
service = "SSH"
open_port = 22

# Print them again in one line
print("Updated service:", service, "on port", open_port)