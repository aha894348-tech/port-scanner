# scanner.py
import socket

def scan_port(host, port):
    #Try to connect to a single port. Return True if open.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # to prevent connect for searching for too long

    try:
        result = sock.connect_ex((host, port))
        # connect_ex returns 0 on success, error code otherwise
        return result == 0
    finally:
        sock.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    for port in [22, 80, 443, 9999]:
        status = "OPEN" if scan_port(host, port) else "closed"
        print(f"port {port}: {status}")
