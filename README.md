import socket

def port_scanner(target, ports):
    print(f"🔍 Scanning target: {target}")
    for port in ports:
        try:
            # Create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            result = sock.connect_ex((target, port))  # Returns 0 if port is open

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")

if _name_ == "_main_":
    target = input("Enter target IP (e.g. 127.0.0.1): ")
    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 8080]  # Common ports
    port_scanner(target, ports)
