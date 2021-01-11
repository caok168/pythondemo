import paramiko

jssh = paramiko.SSHClient()
jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jssh.connect('192.168.11.92', 22, 'lynxi', 'lx123456')

print("=====================")

# jssh = paramiko.SSHClient()
# jssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# key = paramiko.RSAKey.from_private_key_file("/tmp/id_rsa")
# jssh.connect('192.168.11.92', 22, 'lynxi', pkey=key)

stdin, stdout, stderr = jssh.exec_command('ls /home/lynxi')
# print(stdin.read())
print(stdout.read())
print(stderr.read())
