from flask import Flask, request, jsonify
import pika
import uuid, sys
import time




'''
task_queue机制  因为有耗时操作，无需等待服务端返回数据
'''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False 
import uuid, json
# import requests, grequests

def add_app(app: Flask):
    # @app.route('/rabbitmq/round')
    # def round():
    #     api_url = 'http://127.0.0.1:5000/rabbitmq/server'
    #     req_list = [grequests.get(api_url),
    #                 grequests.get(api_url),
    #                 grequests.get(api_url),
    #                 grequests.get(api_url)]
    #     print('*******')
    #     grequests.map(req_list)
        
    #     return 'ok'
        # for i in range(3):
        #     print('****', i)
        #     requests.get(api_url)
            
    @app.route('/rabbitmq/server')
    def server(): 
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')


        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            time.sleep(3)
            print(" [x] Done")
            ch.basic_ack(delivery_tag=method.delivery_tag)


        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='task_queue', on_message_callback=callback)

        channel.start_consuming()

    @app.route('/rabbitmq/client', methods=['POST'])
    def client():  
        connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        message = ' '.join(sys.argv[1:]) or "Hello World!"
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent %r" % message)
        connection.close()
        return 'ok'

    return app

if __name__=='__main__':
    # app.run(debug=False,host='0.0.0.0')
    app = add_app(app)
    app.run(debug=True,host='127.0.0.1')

''' 
cd test.py目录
python -m test1
'''