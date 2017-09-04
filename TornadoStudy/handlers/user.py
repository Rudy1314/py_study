#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: user.py
@time: 2017/9/4 16:07
"""

import TornadoStudy.methods.readdb as mrd
import tornado.web
import tornado.escape
from TornadoStudy.handlers.base import BaseHandler


class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="easy_test", column="*", condition="username", value=username)
        self.render("user.html", users=user_infos)

# def func():
#     pass
#
#
# class Main():
#     def __init__(self):
#         pass
#
#
# if __name__ == '__main__':
#     pass
