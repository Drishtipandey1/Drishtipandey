
"""
Topic 16: Network Scanning with Python
-----------------------------------------
Theory:
- Ethical use only: apne hi lab / permission wali network par!
- Tools/libs: socket (built-in), scapy (advanced, needs install), nmap (external tool).
- We'll implement a simple TCP port scanner using socket (no dependencies).
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host: str, port: int, timeout=0.5) -> bool:
    """Return True if TCP port is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except Exception:
            return False

def scan_range(host: str, ports=range(1, 1025)):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as exe:
        futures = {exe.submit(scan_port, host, p): p for p in ports}
        for fut in as_completed(futures):
            p = futures[fut]
            if fut.result():
                open_ports.append(p)
    return sorted(open_ports)

if __name__ == "__main__":
    target = "127.0.0.1"  # change to your lab host
    print(f"Scanning {target} ...")
    result = scan_range(target, range(1, 200))
    print("Open ports:", result)
