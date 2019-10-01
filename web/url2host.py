from urllib.parse import urlparse
from collections import namedtuple
import socket

REMOTE = namedtuple('REMOTE', ['scheme', 'hostname', 'port'])

url  = 'https://www.baidu.com'
url = urlparse(url)
print(url)
scheme = url.scheme 
address = url.hostname
port = url.port or (443 if scheme=='wss' else 80)
ssl = True if scheme == 'wss' else False
resource = url.path

address = socket.gethostbyname(address)
REMOTE(scheme, address, port)
print(REMOTE.address)