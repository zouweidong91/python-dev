'''
python -m rabbitMQ.producer
'''

import pika
import time

# 建立一个基本的socket
connecttion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connecttion.channel() # 声明一个管道
channel.queue_declare(queue = 'hello') #s声明一个队列
channel.basic_publish(
    exchange = '',
    routing_key = 'hello',
    body = 'Hello World {}'.format(time.strftime('%H:%M:%S',time.localtime(time.time())))
)
print('[x] Sent hello orld', time.strftime('%H:%M:%S',time.localtime(time.time())))
connecttion.close()