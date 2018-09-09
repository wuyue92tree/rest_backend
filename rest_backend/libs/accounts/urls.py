#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wuyue
@contact: wuyue92tree@163.com
@software: IntelliJ IDEA
@file: urls.py
@create at: 2018-09-09 21:55

这一行开始写关于本文件的说明与解释
"""

from django.urls import path, include
from .views import *
from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('profile', ProfileApiView.as_view())

urlpatterns = [
    path('profile/', ProfileApiView.as_view()),
    path('initToken/', InitToken.as_view()),
    path('getToken/', GetToken.as_view())
]
