'''
建造者模式 或 生成器模式
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
很常用
'''

from abc import ABC, abstractmethod
from typing import Any

class Build:
    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass

class Product1:
    def __init__(self):
        self.parts = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")

class ConcreteBuild1(Build):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()


    # 客户端拿到product后，build通常会生成下一个product，因此需要将其重置
    @property
    def get_product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def build_part_a(self):
        self._product.add("partA")
        
    def build_part_b(self):
        self._product.add("partB")

    def build_part_c(self):
        self._product.add("partC")      


class Director:

    # 特殊用法  可以不用在初始化实例时传入build
    def __init__(self): 
        self._build = None

    @property
    def build(self):
        return self._build

    @build.setter
    def build(self, build):
        self._build = build


    
    def build_minimal_viable_product(self):
        self.build.build_part_a()

    def build_full_featured_product(self):
        self.build.build_part_a()
        self.build.build_part_b()
        self.build.build_part_c()

director = Director()
build = ConcreteBuild1()
director.build = build

director.build_full_featured_product()
build.get_product.list_parts()

print('\n')
director.build_minimal_viable_product()
build.get_product.list_parts()