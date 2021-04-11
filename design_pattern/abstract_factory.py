'''
抽象工厂
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类
抽象工厂可以配合反射依赖注入技术大大降低代码量

什么是系列对象：例如有这样的一组对象： 运输工具+引擎+控制器。它科能有几个变体：
1、汽车+内燃机+方向盘
2、飞机+喷气式发动机+操纵杆
如果你的程序中并不涉及产品系列的话，那就不需要抽象工厂，直接用简单工厂即可

工厂的概念： 最常用的情况， 工厂创建的是对象
'''
from abc import ABC, abstractmethod

# 不同数据库分别创建 user和department表

# 工厂类  创建一些类产品实例
class AbstractFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def create_department(self):
        pass

class SqlServerFactory(AbstractFactory):
    def create_user(self):
        return SqlServerUser()

    def create_department(self):
        return SqlServerDepartment()

class AccessFactory(AbstractFactory):
    def create_user(self):
        return AccessUser()

    def create_department(self):
        return AccessDepartment()


# 产品类 user
class AbstractUser(ABC):
    @abstractmethod
    def insert(self, user) -> None:
        pass

    @abstractmethod
    def get_user(self, id):
        pass

class SqlServerUser(AbstractUser):
    def insert(self, user: AbstractUser) -> None:
        print("SqlServer中给User增加一条记录")

    def get_user(self, id) -> AbstractUser:
        print("SqlServer中根据id得到一条User记录")

class AccessUser(AbstractUser):
    def insert(self, user: AbstractUser) -> None:
        print("Access中给User增加一条记录")

    def get_user(self, id) -> AbstractUser:
        print("Access中根据id得到一条User记录")


# department
class AbstractDepartment(ABC):
    @abstractmethod
    def insert(self, department) -> None:
        pass

    @abstractmethod
    def get_department(self, id):
        pass

class SqlServerDepartment(AbstractDepartment):
    def insert(self, department: AbstractDepartment) -> None:
        print("SqlServer中给Department增加一条记录")

    def get_department(self, id) -> AbstractDepartment:
        print("SqlServer中根据id得到一条Department记录")

class AccessDepartment(AbstractDepartment):
    def insert(self, department: AbstractDepartment) -> None:
        print("Access中给Department增加一条记录")

    def get_department(self, id) -> AbstractDepartment:
        print("Access中根据id得到一条Department记录")


# client
class User:
    name = 'zwd'
    age = '30'
class Department:
    room = '401'

user = User()
department = Department()

factory = AccessFactory()
# factory = SqlServerFactory()
i_u = factory.create_user()
i_u.insert(user)
i_u.get_user(1)


i_d = factory.create_department()
i_d.insert(department)
i_d.get_department(1)
