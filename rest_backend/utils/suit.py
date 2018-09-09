#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wuyue
@contact: wuyue92tree@163.com
@software: PyCharm
@file: suit.py
@create at: 2018-04-29 11:58

这一行开始写关于本文件的说明与解释
"""

from django.contrib import admin
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

admin.AdminSite.site_header = 'rest_backend后台管理'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('认证和授权', children=[
            ChildItem(model='accounts.user'),
            ChildItem(model='auth.group'),
            ChildItem(model='authtoken.token'),
        ], icon='fa fa-users'),
        ParentItem('设置', children=[
            # ChildItem('修改密码', url='admin:password_change'),
            ChildItem('API接口文档', url='/api/docs', target_blank=True),

        ], align_right=True, icon='fa fa-cog'),
    )
