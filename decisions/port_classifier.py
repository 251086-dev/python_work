# port_classifier.py
# Classify a port number and check standard services.

port = int(input("Port: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
    if port <= 1023:
        range_name = "system"
    elif port <= 49151:
        range_name = "user"
    else:
        range_name = "dynamic or private"

    message = f"Range: {range_name}"

    if port == 22:
        message += " Service: ssh"
    elif port == 80:
        message += " Service: http"
    elif port == 443:
        message += " Service: https"

    print(message)