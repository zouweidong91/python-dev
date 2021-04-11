'''
外观模式
为子系统的一组接口提供一个统一的界面，此模式定义了一个高层接口，使得这个子系统更加易用
经常使用
'''


class Facade:
    '''
    外观类 它需要了解所有子系统的方法和属性
    '''
    def __init__(self, subsystem1, subsystem2):
        self.subsystem1 = subsystem1 or SubSystem1()
        self.subsystem2 = subsystem2

    def operation(self):
        result = []
        result.append(self.subsystem1.operation1())
        result.append(self.subsystem2.operation1())
        result.append(self.subsystem1.operation2())
        result.append(self.subsystem2.operation2())
        return '\n'.join(result)


class SubSystem1:
    def operation1(self):
        return 'SubSystem1: ready'

    def operation2(self):
        return 'SubSystem1: go'

class SubSystem2:
    def operation1(self):
        return 'SubSystem2: ready'

    def operation2(self):
        return 'SubSystem2: go'

subsystem1 = SubSystem1()
subsystem2 = SubSystem2()
print(Facade(subsystem1, subsystem2).operation())

'''

'''