'''
python -m rabbitMQ.producer
'''

import pika

# 建立一个基本的socket
connecttion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connecttion.channel() # 声明一个管道
channel.queue_declare(queue = 'hello') #s声明一个队列
channel.basic_publish(
    exchange = '',
    routing_key = 'hello',
    body = 'Hello World'
)
print('[x] Sent hello world')
connecttion.close()