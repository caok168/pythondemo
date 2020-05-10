
import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host,80))
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8"))
            break
        except IOError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    print(data)
    client.close()

if __name__ == "__main__":
    get_url("https://www.baidu.com")

