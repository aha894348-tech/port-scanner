import socket
import sys

def resolve_host(host):
    #Turn a hostname into an IP. Raises if it fails.
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error: could not resolve '{host}'")
        sys.exit(1)

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    try:
        return sock.connect_ex((host, port)) == 0
    finally:
        sock.close()

def scan_range(host, start, end):
    open_ports = []
    for port in range(start, end + 1):
        if scan_port(host, port):
            open_ports.append(port)
            print(f"  [OPEN] {port}")
    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    host = resolve_host(sys.argv[1])
    start, end = int(sys.argv[2]), int(sys.argv[3])

    print(f"Scanning {host} ports {start}-{end}...")
    results = scan_range(host, start, end)
    print(f"\nDone. {len(results)} open ports.")
