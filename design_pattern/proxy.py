'''
代理模式
为其他对象提供一种代理以控制对这个对象的访问

使用场景
远程代理： 为一个对象的地址空间提供局部代表
虚拟代理: 根据需要创建开销较大的对象
保护代理： 对象应该具有不同的访问权限，控制对原始对象的访问
智能指引： 访问对象时执行一些附加操作

case:
了解一个班级情况： 人数和学生成绩
人数不需要权限  学生成绩需要权限
'''

class NotFindError(Exception):
    def __init__(self, msg):
        self.msg = msg

class RealSubject:
    def __init__(self):
        self.score = {
            "张三": 90,
            "李四": 77,
            "王五": 80
        }

    def num_students(self):
        print(f'the num of students is {len(self.score)}')

    def get_score(self, name):
        print(f'the score of {name} is {self.score.get(name)}')

class Proxy:
    def __init__(self):
        self.default_pwd = '123'
        self.real_sub = RealSubject()
    
    def num_students(self):
        self.real_sub.num_students()

    def get_score(self, name):
        print(f'you are visiting {name} score...')
        passwd = input("Please input password: ")
        
        if passwd == self.default_pwd:
            if name in self.real_sub.score:
                self.real_sub.get_score(name)
            else:
                raise NotFindError('The student is not found')
        else:
            raise ValueError("the pwd you provided is wrong")

def client():
    proxy = Proxy()
    proxy.get_score("张三")
    
client()


'''
python design_pattern\proxy.py
'''