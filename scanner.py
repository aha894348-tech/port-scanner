import socket
import sys
import argparse

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
   parser = argparse.ArgumentParser(description="TCP port scanner")
   parser.add_argument("host", help="hostname or IP to scan")
   parser.add_argument("start", type=int, help="first port")
   parser.add_argument("end", type=int, help="last port")
   args = parser.parse_args()

   host = resolve_host(args.host)
   start, end = args.start, args.end    

   print(f"Scanning {host} ports {start}-{end}...")
   results = scan_range(host, start, end)
   print(f"\nDone. {len(results)} open ports.")
