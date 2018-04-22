#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wuyue
@contact: wuyue92tree@163.com
@software: PyCharm
@file: database_router.py
@create at: 2018-04-22 12:53

这一行开始写关于本文件的说明与解释
"""

from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.
    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.
    Settings example:
    DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
    """

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure that apps only appear in the related database."""

        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None
