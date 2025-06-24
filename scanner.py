import socket

def scan_ports(domain, port_range=(1, 1024)):
    print(f"Scanning {domain} for open ports {port_range[0]} to {port_range[1]}...")
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((domain, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
        except socket.error:
            pass
        finally:
            sock.close()
    return open_ports

if __name__ == "__main__":
    domain = input("Enter domain or IP to scan: ")
    start_port = int(input("Start port (default 1): ") or 1)
    end_port = int(input("End port (default 1024): ") or 1024)
    scan_ports(domain, (start_port, end_port))
