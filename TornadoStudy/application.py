#!/usr/bin/env python
# coding=utf-8

from TornadoStudy.url import url

import tornado.web
import os

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
        cookie_secret="tSfhZlkKSxyewJH7qDb1XRJ8dQyGCkOIi38RM/LayhY=",
        xsrf_cookies=True,
        login_url='/',
        debug=True
)

application = tornado.web.Application(
        handlers=url,
        **settings
)
