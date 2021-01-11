import telnetlib

tm = telnetlib.Telnet(host='192.168.11.17', port=22, timeout=4)
aa = tm.read_until(b'\n', timeout=5)
print(aa)

