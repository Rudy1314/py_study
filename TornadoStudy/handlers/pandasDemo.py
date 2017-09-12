#!/usr/bin/env python
# encoding: utf-8

"""
@desc 数据处理
@version: ??
@author: phpergao
@license: Apache Licence 
@file: pandasDemo.py
@time: 2017/9/12 0:30
"""

from TornadoStudy.handlers.base import BaseHandler
from pandas import Series, DataFrame
import pandas as pd
import csv


class pandasHandler(BaseHandler):
    def get(self):
        print(1)
        s = Series([100, 'PYTHON', 'Soochow', 'Qiwsir'], index=['hello', 'world', 'test', 'name'])
        print(s)


s = Series([100, 'PYTHON', 'Soochow', 'Qiwsir'], index=['hello', 'world', 'test', 'name'])
# print(s)
# print(pd.isnull(s))
# print(s.isnull())
# 二维的数据结构
data = {"name": ["yahoo", "google", "facebook"], "marks": [200, 400, 800], "price": [9, 3, 7]}
# f1 = DataFrame(data)
# columns规定
f1 = DataFrame(data, columns=['name', 'marks', 'price'])
# print(f1)
# with open("../statics/file/marks.csv") as f:
#     for line in f:
#         print(line)
# print(dir(csv))

# csv_reader = csv.reader(open("../statics/file/marks.csv"))
# for row in csv_reader:
#     print(row)
marks = pd.read_csv("../statics/file/marks.csv")
print(marks)
