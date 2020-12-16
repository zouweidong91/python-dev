
from rpc import rpcserver

def add(a, b, c=10):
    sum = a + b + c
    return sum

s = rpcserver.RPCServer()
s.register_function(add)  # 注册方法
s.loop(5000)


'''
python -m rpc.server
'''