import socket

'''
python -m front_end.socket_server
'''

'''该socket服务端 所有web框架的本质'''
def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes('HTTP/1.1 200 OK\r\n\r\n', encoding='utf8'))
    client.send(bytes('<h1 style="background-color:red">Hello, Zou<h1>', encoding='utf8'))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5) 
    # 传入的值指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。

    while True:
        connecttion, adress = sock.accept()
        handle_request(connecttion)
        connecttion.close()

if __name__ == "__main__":
    
    main()