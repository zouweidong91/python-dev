import socket, json


class TCPClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, data):
        self.sock.send(data)

    def recv(self, length):
        return self.sock.recv(length)


class RPCStub(object):
    '''当实例不存在相关属性时执行该方法'''
    def __getattr__(self, function:str):
        def _func(*args, **kwargs):
            d = {
                'method_name': function,
                'method_args': args,
                'method_kwargs': kwargs
            }
            
            self.send(json.dumps(d).encode('utf8')) # 发送数据
            data = self.recv(1024) # 接受方法执行后返回的结果
            return data

        # setattr(self, function, _func)
        return _func


class RPCClient(TCPClient, RPCStub):
    pass
