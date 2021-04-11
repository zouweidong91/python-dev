'''
策略模式
适用于用多种算法解决一个问题，其最主要特性是能在运行时透明地切换算法

案例：
商场推出多种促销方案，一种是直接打9折，另一种是满1000元打8折再送50
'''

from abc import ABC, abstractmethod
from typing import List, Dict
List[int]  # 标记数组里的元素类型
Dict[str, str]  # 字典中键值的数据类型

class Strategy(ABC):

    # 策略接口声明了不同版本算法间的共有操作，上下文会使用该接口调用具体策略定义的算法
    @abstractmethod  # 抽象方法必须在子类实现
    def discount(self, order):
        pass

class StrategyA(Strategy):
    def discount(self, order):
        return order.price * 0.1

class StrategyB(Strategy):
    def discount(self, order):
        return order.price * 0.2 + 50  

class OrderContext:
    
    # 上下文通常会通过构造含函数类接受策略对象，同时提供设置器以便在运行时切换策略
    def __init__(self, price, strategy: Strategy=None):
        self.price = price
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    # 设置器以便在运行时切换策略
    def strategy(self, strategy):
        self._strategy = strategy

    def price_with_discount(self):
        if self._strategy:
            discount = self._strategy.discount(self)

        else:
            discount = 0

        pay = self.price - discount
        print(f'折扣策略{type(self._strategy).__name__}, 原价: {self.price}, 折扣价: {pay}')
        
        return pay

def main():
    order = OrderContext(1000)
    order.price_with_discount()

    # 切换策略
    st = StrategyA()
    order.strategy = st
    order.price_with_discount()
    
    st = StrategyB()
    order.strategy = st
    order.price_with_discount()
    

main()

    
    

'''
python design_pattern\strategy.py
'''

