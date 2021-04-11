'''
工厂方法
定义一个用以创建对象的接口，让子类决定实例化哪一个类。工厂方法使类的实例化延迟到其子类工厂方法中
而简单工厂模式优点是在工厂类中包含了必要的逻辑判断，根据客户端的选择动态实例化相关的类，但是增加新的运算时就要修改原有的工厂类

'''
from abc import ABC, abstractmethod

# 具体操作加减乘除类
class Operation(ABC):
    @staticmethod
    def get_rst(self, s, y):
        pass

class OperationAdd(Operation):
    def get_rst(self, x, y):
        return x + y
        
class OperationSub(Operation):
    def get_rst(self, x, y):
        return x - y
        
class OperationMul(Operation):
    def get_rst(self, x, y):
        return x * y   

class OperationDiv(Operation):
    def get_rst(self, x, y):
        return x / y
        

# 工厂类
class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
class AddFactory(Factory):
    def factory_method(self) -> Operation:
        return OperationAdd()

class SubFactory(Factory):
    def factory_method(self) -> Operation:
        return OperationSub()

class MulFactory(Factory):
    def factory_method(self) -> Operation:
        return OperationMul()

class DivFactory(Factory):
    def factory_method(self) -> Operation:
        return OperationDiv()


oper_factory = SubFactory()
oper_obj = oper_factory.factory_method()
rst = oper_obj.get_rst(87,3)
print(f'rst: {rst}')

'''
python design_pattern\factory_method.py
'''