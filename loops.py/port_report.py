# port_report.py
# Show the IANA range of every port from start to end.
start = int(input("Start port: "))
end = int(input("End port: "))

checked = 0
for port in range(start, end + 1):
    if port <= 1023:
        print(f"{port}: system")
    elif port <= 49151:
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")
    checked += 1

print(f"Ports checked: {checked}")