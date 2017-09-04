#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: operation.py
@time: 2017/9/4 10:38
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

    # 问题一:输出下面的样式 1,2,3,4,5,6,7,8,9,10
n = 10

for i in range(1, n + 1):
    if i < n:
        print(i, ',')
    else:
        print(i)

# 代码一:一个几M的文本文件，需要每隔5行写到新的文件中。

with open('resources/laravel-test.log', 'rb')as f1, open('resources/laravel-write.log', 'wb') as f2:
    i = 0

    for line in f1:
        i += 1
        if i % 5 == 0:
            line.decode('utf-8')
            f2.write(line)
# 代码二： 请问一个日志文本文件有2000行，我要提取其中的100行到200行，怎么做？
f3 = open('resources/laravel-test-1.log', 'rb')
# ab追加方式  wb 直接覆盖
f4 = open('resources/laravel-write-1.log', 'ab')
while True:
    line = f3.readline()
    i += 1
    if 100 <= i <= 200:
        f4.write(line)
    if i > 200:
        break
    if not line:
        break
f3.close()
f4.close()
