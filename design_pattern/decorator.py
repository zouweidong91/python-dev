'''
需要给给一个类或者一个对象增加一些行为。一般情况下使用继承和关联两种方式来实现。
其中使用关联这种方式来实现并符合一定的设计规范的我们称之为装饰器模式
和继承相比,装饰模式可以在不需要创造更多子类的情况下，将对象的功能加以扩展。这就是装饰模式的模式动机
'''
class Beverage(object):
    '''所有类的基类'''
    def __init__(self):
        self.description = 'unKnown Beverage'
    def get_description(self):
        return self.description
    def cost(self):
        pass

class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = 'HouseBlend'
    def cost(self):
        return 1.99

class Espresso(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = 'HouseBlend'
    def cost(self):
        return 1.39

class CondimentDecorator(Beverage):
    pass

class Milk(CondimentDecorator):
    #这里传入被装饰者，可以是咖啡组件，也可以是已经被mocha或其他调料装饰过的咖啡组件，主要
    #看装饰者在装饰过程中的位置
    def __init__(self,beverage:Beverage):
        super(Milk, self).__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ' Milk'
    def cost(self):
        return self.beverage.cost() + .2
    
class Mocha(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        super(Mocha, self).__init__()
        self.beverage = beverage
    def get_description(self):
        return self.beverage.get_description() + ' Mocha'
    def cost(self):
        return self.beverage.cost() + .3


if __name__ == "__main__":
    #先建立一个咖啡组件的实例
    beverage = HouseBlend()
    #先被milk装饰一遍
    beverage = Milk(beverage)
    #再被mocha装饰一遍
    beverage = Mocha(beverage)

    print('{0}:{1}'.format(beverage.get_description(), '%.3f'%beverage.cost()))

