import paramiko
import datetime
import os

hostname = '服务器ip'
username = 'root'
password = '服务器密码'
port = 22  # 配置信息可以写到配置文件中


# loacl_file是要上传的本地文件路径
# remote_path是要上传到服务器上指定文件的路径
def upload(local_file, remote_path):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print('开始上传文件%s ' % datetime.datetime.now())

        try:
            sftp.put(local_file, remote_path)
        except Exception as e:
            sftp.mkdir(os.path.split(remote_path)[0])
            sftp.put(local_file, remote_path)
            print("从本地： %s 上传到： %s" % (local_file, remote_path))
        print('文件上传成功 %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    local_file = r'/home/shl/dataETL/timings/words/word_pos.csv'
    remote_path = os.path.join('/home/', "word_pos.csv")
    upload(local_file, remote_path)