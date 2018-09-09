#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wuyue
@contact: wuyue92tree@163.com
@software: PyCharm
@file: middleware.py
@create at: 2018-07-28 23:05

这一行开始写关于本文件的说明与解释
"""

from django.utils.deprecation import MiddlewareMixin


class TokenAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.GET.get('token'):
            request.META['HTTP_AUTHORIZATION'] = 'Token %s' % request.GET.get(
                'token')
