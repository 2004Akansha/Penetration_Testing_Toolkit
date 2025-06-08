import socket

def scan_ports(target_ip, ports):
    open_ports = []
    print(f"[+] Starting port scan on {target_ip}")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                    open_ports.append(port)
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")
    return open_ports
