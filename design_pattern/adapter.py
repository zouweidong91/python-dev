'''
适配器模式
将一个类的接口转换为客户希望的另一个接口
使原本由于接口不兼容而不能一起工作的那些类可以一起工作
适配器模式属于无奈之举
'''

class Target:
    def request(self):
        return "一般请求"

class Adaptee:
    def specific_request(self):
        return "特殊的请求"

class Adapter(Target, Adaptee):
    def request(self):
        return self.specific_request()

# clien

target = Target()
print(target.request())

adapter = Adapter()
print(adapter.request())


