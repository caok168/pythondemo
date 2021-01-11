import pexpect

res = pexpect.run("ls /home/lynxi")

print(str(res))

chk = pexpect.spawn('ls -l /tmp/')

chk = pexpect.spawn('ls', ['-l', '/tmp/'])

ssh_k = pexpect.spawn('ssh lynxi@192.168.11.92 -p22')
ssh_k.expect("password:")



