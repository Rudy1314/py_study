#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: db.py
@time: 2017/9/3 17:24
"""

# 数据库链接
import pymysql

# db = pymysql.connect("192.168.56.101", "root", "shopncpw", "easycms")
db = pymysql.connect("192.168.56.102", "root", "shopncpw", "cms")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
