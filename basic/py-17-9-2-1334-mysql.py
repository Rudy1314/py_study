#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: py-17-9-2-1334-mysql.py
@time: 2017/9/2 13:34
"""

# def func():
#     pass
#
#
# class Main():
#     def __init__(self):
#         pass


# 数据库链接
import pymysql

db = pymysql.connect("192.168.56.102", "root", "shopncpw", "cms")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# cursor.execute("SELECT * FROM easy_user")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print(data)
# print("Database version : %s " % data)

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
#
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()


# 数据库查询

# 关闭数据库连接
db.close()
