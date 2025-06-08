from modules import port_scanner, brute_forcer

def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        ip = input("Enter target IP: ")
        ports = list(map(int, input("Enter ports (comma-separated): ").split(',')))
        port_scanner.scan_ports(ip, ports)

    elif choice == '2':
        ip = input("Enter target IP: ")
        username = input("Enter SSH username: ")
        wordlist = "wordlists/passwords.txt"
        brute_forcer.brute_force_ssh(ip, username, wordlist)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
