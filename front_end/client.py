
import socket

client = socket.socket()
host = socket.gethostname()
port = 12345

client.connect((host, port))

data = client.recv(1024)  # 接受从服务端返回的数据  如果大于1024字节，则使用while循环
print(data.decode())  # 由于是字节流传输，需要解码
client.close()

'''
python -m front_end.client
'''