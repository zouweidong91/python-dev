from flask import Flask, request, jsonify
import pika
import uuid
import time, math
import grequests
'''
需要等待服务端返回数据，因此需要开启多个服务端和多个客户端
'''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
def make_app() -> False:
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/name/<name>')
    def my_name(name):
        return 'my name is {}'.format(name)
        # http://127.0.0.1:5000/name/zouweidong
        # my name is zouweidong

    @app.route('/test', methods=['POST'])
    def test():
        # postdata = request.form['id']
        postdata = request.get_json()
        print(postdata)
        return jsonify(postdata)

    @app.route('/rabbitmq/send', methods=['POST'])
    def send():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(
            exchange='', 
            routing_key='hello', 
            body='Hello World! {}'.format(time.strftime('%H:%M:%S',time.localtime(time.time()))))
        print(" [x] Sent 'Hello World!'{}".format(time.strftime('%H:%M:%S',time.localtime(time.time())))
        )
        connection.close()
        return 'send ok'
         
    @app.route('/rabbitmq/receive', methods=['POST'])
    def receive():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')


        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        # return 'receive ok'
    return app
        
import uuid, json
import requests
# from .model_ner import ReMatrxNer

# ner_predicator = ReMatrxNer(model_name='ner_finance_negative_aug_v2')

def add_app(app: Flask):
    # @app.route('/rabbitmq/s_round')
    # def round():
    #     api_url = 'http://127.0.0.1:5000/rabbitmq/server'
    #     req_list = [grequests.get(api_url),
    #                 grequests.get(api_url),
    #                 grequests.get(api_url),
    #                 grequests.get(api_url)]
    #     print('*******')
    #     grequests.map(req_list)
        
    #     return 'ok'
            
    @app.route('/rabbitmq/server')
    def server(): # 即发送数据又接收数据
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        channel = connection.channel()

        channel.queue_declare(queue='rpc_queue')

        # def ner_modle(data):
        #     resp_dict = ner_predicator.predict_json(data)
        #     resp_dict = josn.dumps(resp_dict)
        #     return resp_dict
        def ner_api(data):
            api_url = 'http://api.nlp.phbs-ai.wezuzhi.com/predict/ner'
            headers = {'Content-Type': 'application/json'}
            result = requests.post(api_url, data = data, headers=headers)
            return result.text

        def on_request(ch, method, props, body):
            response = ner_api(body)

            ch.basic_publish(exchange='',
                            routing_key=props.reply_to,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_qos(prefetch_count=1) # 消费任务处理完成之前不再接收生产者的任务
        channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

        print(" [x] Awaiting RPC requests")
        channel.start_consuming()

    @app.route('/rabbitmq/client', methods=['POST'])
    def client():  # 即发送数据又接收数据
        data = request.get_data()  # byte
        # print(data)
        class Ner(object):

            def __init__(self):
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost'))

                self.channel = self.connection.channel()

                result = self.channel.queue_declare(queue='', exclusive=True)
                self.callback_queue = result.method.queue

                self.channel.basic_consume(
                    queue=self.callback_queue,
                    on_message_callback=self.on_response,
                    auto_ack=True)

            def on_response(self, ch, method, props, body):
                if self.corr_id == props.correlation_id:
                    self.response = body

            def call(self, data):
                self.response = None
                self.corr_id = str(uuid.uuid4())
                self.channel.basic_publish(
                    exchange='',
                    routing_key='rpc_queue',
                    properties=pika.BasicProperties(
                        reply_to=self.callback_queue,
                        correlation_id=self.corr_id,
                    ),
                    body=data)
                while self.response is None:
                    self.connection.process_data_events()
                return self.response

        ner_rpc = Ner()

        print(" [x] Requesting ner")
        response = ner_rpc.call(data)
        print(" [.] Got ner")
        response = json.loads(response)
        ner_rpc.channel.close()
        return jsonify(response)

    @app.route('/rabbitmq/client_round', methods=['POST'])
    def client_round():  # 即发送数据又接收数据
        data = request.get_json()  # byte
        num = 30
        len_text = len(data['content'])
        req_list = []
        api_url = 'http://127.0.0.1:5000/rabbitmq/client'
        for i in range(math.ceil(len_text/num)):
            _data = json.dumps({'content': data['content'][i*num:(i+1)*num]})
            req_list.append(grequests.post(api_url, data=_data))
        print('*******')
        res_list = grequests.map(req_list)
        res_list = [json.loads(res.text) for res in res_list]
        ner_list, text_list = [], []
        for res in res_list:
            ner_list.extend(res['data'])
            text_list.extend(res['text_list'])
        res_dict = {"data": ner_list, "text_list": data['content']}
        return jsonify(res_dict)

    return app

if __name__=='__main__':
    # app.run(debug=False,host='0.0.0.0')
    app = make_app()
    app = add_app(app)
    # @app.route('/add')
    # def add():
    #     return 'Hello, add!'
    app.run(debug=True,host='127.0.0.1')

''' 
cd test.py目录
python -m test
'''