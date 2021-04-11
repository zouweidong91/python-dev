'''
状态模式
当一个对象的内部状态改变时允许改变其行为，这个对象看起来好像改变了其类
主要是为了解决状态转换的条件表达式过于复杂的情况。把条件判断逻辑转移到表示不同状态的一系列类中
'''

from abc import ABC, abstractmethod

# 上下文类
class Context:
    hour = None

    def __init__(self, state=None):
        self.state = state  # 定义上下文的当前状态

    def request(self):
        self.state.handler(self)

# 状态类  包含了状态转移
class State(ABC):

    @abstractmethod
    def handler(self, context):
        pass

class ConcreteStateA(State):

    # 设置ConcreteStateA的下一个状态时ConcreteStateB
    def handler(self, context):
        if context.hour < 9:
            print(f"当前时间{context.hour}点, 上午")
        else: # 转移状态
            context.state = ConcreteStateB()
            context.request()
        
class ConcreteStateB(State):
    def handler(self, context):
        if context.hour < 17:
            print(f"当前时间{context.hour}点, 下午")
        else: # 转移状态
            context.state = ConcreteStateC()
            context.request()

class ConcreteStateC(State):
    def handler(self, context):
        print("一天结束")


# client
context = Context(ConcreteStateA())
context.hour = 5
context.request()
context.hour = 13
context.request()
context.hour = 5
context.request()