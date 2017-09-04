#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: url.py
@time: 2017/9/2 22:44
@desc:the url structure of website
"""
from TornadoStudy.handlers.index import IndexHandler
from TornadoStudy.handlers.user import UserHandler
from TornadoStudy.handlers.sleep import SeepHandler, SleepHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/seep', SeepHandler),
    (r'/sleep', SleepHandler),

]
