#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: sleep.py
@time: 2017/9/4 17:45
"""
from TornadoStudy.handlers.base import BaseHandler
import time


def func():
    pass


class SleepHandler(BaseHandler):
    def get(self):
        time.sleep(10)
        self.render("sleep.html")


class SeepHandler(BaseHandler):
    def get(self):
        self.render("seep.html")
