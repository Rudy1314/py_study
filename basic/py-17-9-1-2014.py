#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: py-17-9-1-2014.py
@time: 2017/9/1 20:18
"""

#
# def hello(name='tom', age=12):
#     print(name, 'age=', age, 'hello world')
#     return
#
#
# #
# # hello('test',30)
# # int(input('请输入'))
# sumAdd = lambda a, b: a + b
# print(sumAdd(10, 20))


# 打开一个文件
# f = open("tmp/foo.txt", "r")

# # f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
#
# strArr = f.read()
# print(strArr)
#
# # 关闭打开的文件
# f.close()
from urllib import request

response = request.urlopen("https://www.bilibili.com/")  # 打开网站
fi = open("tmp/foo.txt", 'w')  # open一个txt文件
page = fi.write(str(response.read()))  # 网站代码写入
fi.close()  # 关闭txt文件
