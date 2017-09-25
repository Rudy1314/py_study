#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: server.py
@time: 2017/9/2 22:44
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options

from TornadoStudy.application import application

from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http:/  /127.0.0.1:%s" % options.port)
    print("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
