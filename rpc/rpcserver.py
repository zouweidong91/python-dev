
import socket, json

class TCPServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, port):
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(5) # backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量

    def accept_receive_close(self):
        '''获取client信息'''
        (client_socket, address) = self.sock.accept()
        msg = client_socket.recv(1024)
        data = self.on_msg(msg)
        client_socket.sendall(data) # 回传
        client_socket.close()

class JSONRPC:
    def __init__(self):
        self.data = None
    
    def from_data(self, data):
        self.data = json.loads(data.decode('utf8'))

    def call_method(self, data):
        '''解析数据，调用相应的方法执行结果返回'''
        self.from_data(data)
        method_name = self.data['method_name']
        method_args = self.data['method_args']
        method_kwargs = self.data['method_kwargs']
        
        res = self.funs[method_name](*method_args, **method_kwargs)
        data = {"res": res}
        return json.dumps(data).encode('utf8')

class RPCStub:
    def __init__(self):
        self.funs = {}

    def register_function(self, function, name=None):
        '''Server端方法注册，Client端只可调用被注册的方法'''
        if name is None:
            name = function.__name__
        self.funs[name] = function

class RPCServer(TCPServer, JSONRPC, RPCStub):
    def __init__(self):
        TCPServer.__init__(self)
        JSONRPC.__init__(self)
        RPCStub.__init__(self)

    def loop(self, port):
        self.bind_listen(port)
        print("Server listen 5000..")
        # while True:
        for i in range(4):
            self.accept_receive_close()

    def on_msg(self, data):
        return self.call_method(data)