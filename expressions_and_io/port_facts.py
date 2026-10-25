# port_facts.py
# This program counts ports and IPv4 addresses.
# Source 1: RFC 9293 - TCP source and destination ports are 16 bits each.
# Source 2: RFC 791 - IPv4 addresses are four octets (32 bits).

PORT_BITS = 16
IPV4_BITS = 32

number_ports = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
number_ipv4 = 2 ** IPV4_BITS

print(f"Number of ports: {number_ports}")
print(f"Highest port number: {highest_port}")
print(f"Number of IPv4 addresses: {number_ipv4}")