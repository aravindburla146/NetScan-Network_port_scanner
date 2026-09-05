import ipaddress
import socket
import time
from concurrent.futures import ThreadPoolExecutor

def validate_target(target):
    """
    Validate whether the target is a valid IP address or hostname.
    """

    try:
        ipaddress.ip_address(target)
        return True

    except ValueError:
        try:
            socket.gethostbyname(target)
            return True

        except socket.gaierror:
            return False

def get_port_range():
    """
    Ask the user for a valid TCP port range.
    """

    while True:
        try:
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

            if not (1 <= start_port <= 65535):
                print("[ERROR] Start port must be between 1 and 65535.")
                continue

            if not (1 <= end_port <= 65535):
                print("[ERROR] End port must be between 1 and 65535.")
                continue

            if start_port > end_port:
                print("[ERROR] Start port cannot be greater than end port.")
                continue

            return list(range(start_port, end_port + 1))

        except ValueError:
            print("[ERROR] Please enter valid numbers.")

def scan_port(target, port):
    """
    Scan a single TCP port and identify its common service.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            return {
                "port": port,
                "status": "Open",
                "service": service
            }

        return {
            "port": port,
            "status": "Closed",
            "service": "-"
        }

    except socket.error:
        return {
            "port": port,
            "status": "Error",
            "service": "-"
        }

    finally:
        sock.close()


def scan_target(target, ports):
    """
    Scan multiple TCP ports concurrently.
    """

    results = []

    start_time = time.time()

    # Create multiple worker threads
    with ThreadPoolExecutor(max_workers=100) as executor:

        scan_results = executor.map(
            lambda port: scan_port(target, port),
            ports
        )

        for result in scan_results:
            results.append(result)
            if result["status"] == "Open":
                print(
                    f"[OPEN] Port {result['port']} "
                    f"({result['service']})"
                    )

    end_time = time.time()

    duration = round(end_time - start_time, 2)

    open_ports = sum(
        1 for result in results
        if result["status"] == "Open"
    )

    print("\n-----------------------------")
    print("        SCAN SUMMARY")
    print("-----------------------------")
    print(f"Target       : {target}")
    print(f"Ports scanned: {len(ports)}")
    print(f"Open ports   : {open_ports}")
    print(f"Scan time    : {duration} seconds")
    print("-----------------------------")

    return {
    "results": results,
    "duration": duration
}


if __name__ == "__main__":

    target = input("Enter target IP address or hostname: ").strip()

    if not validate_target(target):
        print("\n[ERROR] Invalid target.")
        print("Please enter a valid IP address or hostname.")
        raise SystemExit

    ports = get_port_range()

    print(f"\nStarting scan on {target}...\n")

    scan_target(target, ports)