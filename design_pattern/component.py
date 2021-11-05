'''
组合模式
可以将对象组合成树状结构，并且能像使用独立对象一样使用它们
对于大多数需要生成树状结构的问题来说，组合都是非常受欢迎的解决方案。组合最主要的功能是能在树状结构上
递归调用方法并对结果进行汇总

需实现叶节点和枝节点
'''

from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    
    def __init__(self, name):
         self.name = name

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass 

    @abstractmethod
    def display(self, depth):
        pass

# 叶节点
class Leaf(Component):
    def add(self, component):
        print("不能添加下级节点")

    def remove(self, component):
        print("不能删除下级节点")
    
    def display(self, depth:int):
        print("-"*depth + self.name)

# 枝节点
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.childern = []

    def add(self, component):
        self.childern.append(component)
    
    def remove(self, component):
        self.childern.remove(component)

    def display(self, depth:int):
        for component in self.childern:
            component.display(depth + 2)
        


root = Composite('root')
root.add(Leaf("Leaf A"))
root.add(Leaf("Leaf B"))


comp = Composite("Composite X")
comp.add(Leaf("Leaf XA"))
comp.add(Leaf("Leaf XB"))
root.add(comp)


comp = Composite("Composite XY")
comp.add(Leaf("Leaf XYA"))
comp.add(Leaf("Leaf XYB"))

root.add(Leaf("Leaf C"))

leaf = Leaf("Leaf D")
root.add(leaf)
root.remove(leaf)


root.display(2)

'''
python design_pattern\component.py
'''

