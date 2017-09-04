#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: base.py
@time: 2017/9/4 17:06
"""
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
