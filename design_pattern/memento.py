'''
备忘录模式
不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样就可以将该对象恢复到原先保存的状态

在python中，备忘录的基本功能可用序列化来实现
'''

from abc import ABC, abstractmethod
from datetime import datetime
from random import sample

# 发起人类
class Originator:
    
    def __init__(self, state):
        self.state = state

    # 创建备忘录
    def create_memento(self):
        return Memento(self.state)

    # 设置状态
    def set_memento(self, memento):
        self.state = memento.state

    def show(self):
        print("当前状态", self.state)


# 备忘录类  除了Originator以外的其他类不能访问内部细节
class Memento:
    def __init__(self, state):
        self.state = state

# 管理者类
class Caretaker:
    def __init__(self, memento):
        self.memento = memento


if __name__ == "__main__":
    originator = Originator(state = "on")
    originator.show()
    
    memento = originator.create_memento()
    caretaker = Caretaker(memento)

    # 修改状态
    originator.state = "off"
    originator.show()

    # 复原状态
    originator.set_memento(caretaker.memento)
    originator.show()


'''
python design_pattern\memento.py
'''