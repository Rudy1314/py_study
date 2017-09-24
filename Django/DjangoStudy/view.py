#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: view.py
@time: 2017/9/24 11:55
"""

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World RU!'
    context['one'] = 'one'
    context['test'] = 'I am TEST , Hello World RU!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello World !")
