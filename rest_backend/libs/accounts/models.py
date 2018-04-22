# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class User(AbstractUser):
    GENDER_CHOICE = (
        (0, _('unknown')),
        (1, _('male')),
        (2, _('female')),
    )
    nickname = models.CharField(max_length=255, blank=True, verbose_name=_('nickname'))
    phone = models.BigIntegerField(blank=True, null=True, verbose_name=_('phone'))
    head_avatar = models.ImageField(
        upload_to='./avatars',
        default="./avatars/default.png",
        blank=True,
        verbose_name=_('head_avatar'))
    head_oauth_avatar = models.URLField(blank=True, verbose_name=_('head_oauth_avatar'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    gender = models.IntegerField(blank=True, null=True, choices=GENDER_CHOICE, verbose_name=_('gender'))
    birthday = models.DateField(default=timezone.now, verbose_name=_('birthday'))
    activate_key = models.SlugField(max_length=255, blank=True, verbose_name=_('activate_key'))

