import socket

def scan_ports(host):
    print(f"Scanning {host}...")
    for port in range(20, 1025):  # common ports
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            sock.close()
        except:
            pass

target = input("Enter target IP: ")
scan_ports(target)
