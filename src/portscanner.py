from ipaddress import ip_address
import socket
import termcolor



def scan(target, ports):
    print('\n' + 'Starting scan for ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ip_address,port): 
    try:
        sock = socket.socket()
        sock.connect((ip_address,port))
        print(termcolor.colored(f"[+] Port {port} is Open", 'green'))
    except:
        print(termcolor.colored(f"[+] Port {port} is Closed", 'red'))

targets = input("[*] Enter targets to scan (split them by ','):")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)