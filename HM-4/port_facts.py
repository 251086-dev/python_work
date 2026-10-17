# number of ports : 65536
# number of ipv4  : 4294967296

PORT_BITS = 16
IPV4_BITS = 32

TCP = 2**PORT_BITS
IPV4 = 2**IPV4_BITS

number_ports = TCP
number_ipv4 = IPV4

print(f"number_ports:\t{number_ports}")
print(f"number_ipv4:\t{number_ipv4}")
