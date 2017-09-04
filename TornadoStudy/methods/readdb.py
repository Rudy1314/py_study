#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: readdb.py
@time: 2017/9/3 18:17
"""

from TornadoStudy.methods.db import *


def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines


def select_columns(table, column):
    sql = "select " + column + " from " + table
    cursor.execute(sql)
    lines = cursor.fetchall()
    return lines
