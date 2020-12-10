import collections
from functools import wraps

#
# def foo(func):
#     # @wraps(func)
#     def inner(*args,**kwargs):
#         print("decrator---1----------------")
#         res = func(*args,**kwargs)
#         print('---res---',res)
#         print("decrator---2----------------")
#         return  res
#     return inner
#
# @foo
# def f_main():
#     print("--main--")
#     return 666
#
# print(f_main.__name__)
# print('process main function')
# f_main()

# import abc
#
# class AllFile(metaclass=abc.ABCMeta):
#     all_type='file'
#
#     @abc.abstractmethod
#     def read(cls):
#         pass
#
#     @abc.abstractmethod
#     def write(self):
#         pass
#
# class Txt(AllFile):
#     def read(self):
#         print("readd-----------")
#         return 666
#
#     def write(self):
#         print('write--------')
#
#
# t1 = Txt()
# print(t1.read())

# import threading
#
# class Singleton(object):
#     instance = None
#     lock = threading.Lock()
#
#     def __new__(cls):
#         if not cls.instance :
#             # cls.instance = object.__new__(cls)
#             cls.instance = super().__new__(cls)
#
#         return cls.instance
#
#
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1)
# print(obj2)
import pytest


# def func(x):
#     return x+1
#
# def test_answer():
#     assert func(3) == 5
#



from collections import namedtuple
#
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# print(Task)

Task.__new__.__defaults__=(None,None,False,None)

# def test_defaults():
#     t1 = Task()
#     t2 =Task(None,None,False,None)
#     assert t1==t2
#
#
# @pytest.mark.mark1
# def test_member_access():
#     print("***mark1****")
#     t = Task('buy milk','brain')
#     print("t---",t)
#     assert t.summary == 'buy milk'
#     assert t.owner == 'brain'
#     assert (t.done,t.id) == (False,None)
#
# def test_asdict():
#     t_task = Task('do something','okken',True,21)
#     t_dict = t_task._asdict()
#     # print(t_dict)
#     # print(dict(t_dict))
#     expected  ={
#         'summary':'do something',
#         'owner':'okken',
#         'done':True,
#         'id':21
#     }
#     assert t_dict == expected
#
# def test_replace():
#     print("**************")
#     t_before = Task('finish book','brain',False)
#     t_after  =t_before._replace(id=10,done=True)
#     t_expected = Task('finish book','brain',True,10)
#     assert t_after ==t_expected

data =[('zhangsan','男'),('李四','女'),('赵武','男')]
data1  =['case1','case2','case3']

@pytest.mark.parametrize('name,sex',data,ids=data1)
def test_name(name,sex):
    print(name,sex)
    assert name == 'zhangsan'


# import pytest
#
# @pytest.fixture()
# def some_data():
#     return 42
#
# def test_some_data(some_data):
#     print("----",some_data)
#     assert some_data==42
