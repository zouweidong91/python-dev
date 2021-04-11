'''
原型模式
从一个实例对象再创建另外一个可定制的对象  分为浅拷贝和深拷贝
'''

import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent

class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
    
    def __copy__(self):
        '''create a shallow copy   当执行copy.copy(object)时调用此方法
        '''
        # first create copies of the nested objects
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # then clone the object itself
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)

        # print(self.__dict__)
        new.__dict__.update(self.__dict__)
        # print(new.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        '''create a deep copy   当执行copy.deepcopy(object)时调用此方法
        memo 防止存在循环引用时无限递归copy
        '''
        # first create copies of the nested objects
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # then clone the object itself
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)

        # new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new

list_of_objects = [1,{1,2,3}, [1,2,3]]
cirular_ref = SelfReferencingEntity()
component = SomeComponent(23, list_of_objects, cirular_ref)

cirular_ref.set_parent(component)

# shallow copy
shallow_copied_component = copy.copy(component)
shallow_copied_component.some_list_of_objects[-1] = 'another object'
print(component.some_list_of_objects[-1])

component.some_list_of_objects[1].add(4)
print(shallow_copied_component.some_list_of_objects[1])


# deepcopy
deep_copied_component = copy.deepcopy(component)
deep_copied_component.some_list_of_objects[-1] = 'one more object'
print(component.some_list_of_objects[-1])

component.some_list_of_objects[1].add(10)
print(deep_copied_component.some_list_of_objects[1])


'''

'''

