import paramiko

HOST_IP = '192.168.11.92'
USER_NAME = 'lynxi'
PASSWORD = 'lx123456'

# 无密钥登陆
# ssh-keygen -t rsa
# ls ~/.ssh/
# scp id_rsa.pub user@host:~/.ssh/authorized_keys


def demo1():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST_IP, 22, USER_NAME, PASSWORD)
    stdin, stdout, stderr = ssh.exec_command('df -h')
    for line in stdout:
        print(line)
    ssh.close()


def demo2():
    t = paramiko.Transport(HOST_IP, 22)
    t.connect(username=USER_NAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('/home/lynxi/aaa', '/home/lynxi/aaa')
    t.close()


def demo3():
    t = paramiko.Transport(HOST_IP, 22)
    t.connect(username=USER_NAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get('/home/lynxi/aaa', '/home/lynxi/bbb')
    t.close()


def demo4():
    private_key_path = '/home/lynxi/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_path)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(HOST_IP, 22, username=USER_NAME, pkey=key)
    stdin, stdout, stderr = ssh.exec_command('df')
    # print(stdout.read())
    for line in stdout:
        print(line)
    ssh.close()


def demo5():
    scp = paramiko.Transport(HOST_IP, 22)
    scp.connect(username=USER_NAME, password=PASSWORD)
    channel = scp.open_session()
    channel.exec_command('touch test.txt')
    channel.close()
    scp.close()


if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    demo5()

