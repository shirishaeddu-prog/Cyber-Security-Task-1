import socket

ip = input("Enter local IP address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]

print("\nScanning:", ip)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ip, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")

    s.close()

print("\nScan completed.")