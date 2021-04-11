'''
观察者模式  发布-订阅模式 事件监听模式
定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象，当这个主题对象状态发生改变时，会通知所有的观察者对象，使他们能够自动更新自己

开放-封闭原则：不修改原有代码
依赖倒转原则： 程序应依赖抽象，不应相互依赖具体  抽象通知者依赖抽象观察者
很流行
'''
from typing import List
from abc import ABC, abstractmethod



class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer):
        pass
        
    @abstractmethod
    def notify(self):
        '''
        notify all observers about an event
        '''
        pass

class ConcreteSubject(Subject):
    _observers = []

    _state: int = None # 当状态更改时通知观察者

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        '''
        Receive update from subject
        '''
        pass

class ConcreteObserverA(Observer):
    def update(self, subject):
        print(f"观察者A的新状态是{subject._state}")


class ConcreteObserverB(Observer):
    def update(self, subject):
        print(f"观察者B的新状态是{subject._state}")

subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject._state = 'XYZ'
subject.notify()

'''

'''