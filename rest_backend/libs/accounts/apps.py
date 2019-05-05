from __future__ import unicode_literals

from django.apps import AppConfig
# from django.utils.translation import gettext_lazy as _

__all__ = ['AccountsConfig']


class AccountsConfig(AppConfig):
    name = 'rest_backend.libs.accounts'
    label = 'accounts'
    verbose_name = '用户中心'
