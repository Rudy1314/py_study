#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: index.py
@time: 2017/9/3 17:23
"""

import tornado.web
import json
import TornadoStudy.methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):
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
            if db_pwd == password:
                self.write(username)
            else:
                self.write("your password was not right.")

        else:
            self.write("There is no thi user.")

            # result = {"username": username, "password": password}
            # self.write(json.dumps(result))
