

from rpc import rpcclient



c = rpcclient.RPCClient()
c.connect('127.0.0.1', 5000)
res = c.add(1, 2, c=3)
print(res)


'''
https://cloud.tencent.com/developer/article/1583439
python -m rpc.client
'''