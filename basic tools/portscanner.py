import socket
import termcolor

def scan (target,ports):
    print(termcolor.colored("[*] Scanning Target "+str(target),"yellow"))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        print(termcolor.colored(("[+] Port Opened "+str(port)) , 'light_cyan'))
        sock.close()
    except:
        pass 


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets","yellow"))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:     
        scan(targets,ports)  