#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: index.py
@time: 2017/9/3 17:23
"""

# import tornado.web
# import json
import tornado.escape
import TornadoStudy.methods.readdb as mrd
from TornadoStudy.handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        user_infos = mrd.select_columns(table="easy_test", column="username")
        one_user = user_infos[0][0]
        self.render("index.html", user=one_user)

    # 处理post请求
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="easy_test", column="*", condition="username", value=username)
        print('the is what the', user_infos)

        if user_infos:
            db_pwd = user_infos[0][2]
            print('the is pwd the', db_pwd)
            if db_pwd == password:
                # 不加密的cookie
                # self.set_cookie(username, db_pwd)
                # 加密cookie
                # self.set_secure_cookie(username + username, db_pwd)
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("-1")
                # self.write("your password was not right.")

        else:
            self.write("-1")
            # self.write("There is no the user.")

            # result = {"username": username, "password": password}
            # self.write(json.dumps(result))

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))  # 注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

    def postTestNotUse(self):
        username = self.get_argument("username")

        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                # 设置cookie
                self.set_cookie(username, db_pwd)

                self.write(username)
            else:
                self.write("your password was not right.")

        else:
            self.write("There is no thi user.")


class ErrorHandler(BaseHandler):  # 增加了一个专门用来显示错误的页面
    def get(self):  # 但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")
