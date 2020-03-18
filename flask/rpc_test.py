
import  requests, json, grequests, math, time
data ={"content": ["2020年万科对应利润和负债分别为 54亿元和217亿","碧桂园2018年业绩",
                    "碧桂园2018年业绩1",
                    "碧桂园2018年业2","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩",
                    "碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩",
                    "碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩","碧桂园2018年业绩",
                    "碧桂园2018年业绩",'碧桂园2018年业绩']}
t_li = data['content']
data['content'] = t_li*2
def client_round():  # 即发送数据又接收数据
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
    return res_dict

if __name__ == "__main__":
    a = time.time()
    res_dict = client_round()
    # print(res_dict)
    print('content', len(res_dict['text_list']))
    print('res_list', len(res_dict['data']))
    print('cost_time', time.time()-a)
'''
python flask/rpc_test.py
'''