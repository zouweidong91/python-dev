'''

专门通过一个类来负责创建其他类的实例，被创建的实例通常具有相同的父类
'''
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def get_rst(self, s, y):
        return 0


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
        

class OperationFactory:
    @staticmethod
    def create_operation(operation):
        math_dict = {
            "+": OperationAdd,
            "-": OperationSub,
            "*": OperationMul,
            "/": OperationDiv
        }
        
        operation_obj = math_dict.get(operation)()
        return operation_obj


operation_obj = OperationFactory.create_operation('+')
rst = operation_obj.get_rst(8, 9)
print(rst)

'''
python design_pattern\sample_factory.py
'''