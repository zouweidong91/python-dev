'''
模板方法
比较常见，它在基类中定义了一个算法框架，允许子类在不修改结构的情况下重写算法的特定步骤
'''

from abc import ABC, abstractmethod

# 模板类
class Template(ABC):
    
    def template_method(self) -> None:
        '''
        the template method define the skeleton of an algorithm
        '''
        self.base_operation1()
        self.required_operation1()
        self.hook1()
        self.base_operation2()
        self.required_operation2()

    def base_operation1(self):
        print("Template operation 1")

    def base_operation2(self):
        print("Template operation 2")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        '''钩子函数  提供附加的扩展功能
        '''
        pass

# 具体类
class ConcreteClass1(Template):
    def required_operation1(self):
        print("ConcreteClass1 required_operation 1")

    def required_operation2(self):
        print("ConcreteClass1 required_operation 2")

class ConcreteClass2(Template):
    def required_operation1(self):
        print("ConcreteClass2 required_operation 1")

    def required_operation2(self):
        print("ConcreteClass2 required_operation 2")

    def hook1(self):
        print('hook1')
        

ConcreteClass2().template_method()