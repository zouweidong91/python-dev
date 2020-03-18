
'''
python -m rabbitMQ.consumer
'''
import pika

# 建立一个基本的socket
connecttion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connecttion.channel() # 声明一个管道
channel.queue_declare(queue = 'hello') #s声明一个队列

def callback(ch, method, properties, body):
   # print(ch, method, properties)
   print('[x] received %r'%body)

channel.basic_consume(
   queue = 'hello',
   on_message_callback = callback,  # 如果收到消息，就调用callback 处理消息
   
   auto_ack = True
 )
print('[x] waitting for massege')
channel.start_consuming()