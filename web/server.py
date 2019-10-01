import socket

#所有web框架的本质
def handle_request(client):
    buf =  client.recv(1024)
    client.send(b'HTTP/1.1 200 OK\r\n\r\n')
    client.send(b"Hello, Zou")
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)
    while True:
        connection, address = sock.accept() #服务端开启等待连接，没有连接，则一直等待
        handle_request(connection)
        connection.close()# 处理i请求后把当前连接关闭
if __name__ == "__main__":
    main()