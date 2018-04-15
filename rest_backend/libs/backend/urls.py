#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wuyue
@contact: wuyue92tree@163.com
@software: PyCharm
@file: urls.py
@create at: 2018-04-15 17:58

这一行开始写关于本文件的说明与解释
"""

from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='Project API')

router = routers.DefaultRouter()


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/login/', obtain_jwt_token, name='token-login'),
    path('api-docs/', schema_view),
]
