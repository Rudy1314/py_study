#!/usr/bin/env python
# coding=utf-8

from TornadoStudy.url import url

import tornado.web
import os

print('hello python')
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    debug=True
)

application = tornado.web.Application(
    handlers=url,
    **settings
)
