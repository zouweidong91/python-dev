

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # 获取本地主机名
port = 12345
server.bind((host, port))  # 绑定端口

server.listen(5)  # 等待客户端连接， 连接的最大数量

while True:
    client, addr = server.accept()  # s建立客户端连接
    print('连接地址', addr)
    # client.recv(1024)  # 接受一个信息，并指定接受的大小
    client.send(bytes('欢迎访问本机服务', encoding='utf8'))
    client.close()

'''
python -m front_end.server
'''

