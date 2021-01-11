import nmap

nm = nmap.PortScanner()
res = nm.scan(hosts="192.168.11.0/24", arguments="-n -sP -PE")
print(res)

print("==================================================")

hosts = nm.all_hosts()
print(hosts)

for host in hosts:
    print(host)
