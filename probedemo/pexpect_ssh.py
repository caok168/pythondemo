import pexpect


def login_ssh_passwd(port="", user="", host="", passwd=""):
    '''
    函数：用于实现pexpect实现ssh的自动化用户密码登陆
    '''
    if port and user and host and passwd:
        ssh = pexpect.spawn('ssh -p %s %s@%s' % (port, user, host))
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
        index = ssh.expect(["$", pexpect.EOF, pexpect.TIMEOUT])

        if index == 0:
            print("logging in as root!")
            ssh.interact()
        elif index == 1:
            print("logging process exit!")
        elif index == 2:
            print("logging timeout exit!")
    else:
        print("Parameter error!")


def login_ssh_key(keyfile="", user="", host="", port=""):
    """函数：用于实现pexpect实现ssh的自动化密钥登陆"""
    if port and user and host and keyfile:
        ssh = pexpect.spawn('ssh -i %s %s@%s' % (keyfile, port, user, host))
        i = ssh.expect([pexpect.TIMEOUT, 'continue connecting (yes/no)?'], timeout=2)
        if i == 1:
            ssh.sendline('yes\n')
            index = ssh.expect(["#", pexpect.EOF, pexpect.TIMEOUT])
        else:
            index = ssh.expect(["#", pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            print("logging in as root!")
        elif index == 1:
            print("logging process exit!")
        elif index == 2:
            print("logging timeout exit!")
    else:
        print("Parameter error!")


if __name__ == '__main__':
    login_ssh_passwd(port="22", user="lynxi", host="192.168.11.92", passwd="lx123456")
    # login_ssh_key(keyfile='/tmp/id_rsa', port='22', user='root', host='192.168.11.92')
