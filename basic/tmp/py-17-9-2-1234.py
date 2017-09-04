#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: py-17-9-1-2155.py
@time: 2017/9/1 21:55
"""

# 使用with关键字 自动关闭执行之后的文件
# with open("tmp/foo.txt") as f:
#     for line in f:
#         print(line, end="")


# py的面向对象
# class MyClassName:
#     """一个简单的类实例"""
#     i = 123456
#
#     def __init__(self):
#         self.data = []
#
#     def f(self):
#         return "hello world"
#
#
# x = MyClassName()
#
# # 访问类的属性和方法
# print(x.i)
# print(x.f())

# self 代表类的实例，而非类
# import datetime

from datetime import date

now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

exit()


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()
