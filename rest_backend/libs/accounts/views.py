# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token


# Create your views here.


class ProfileSerializer(serializers.ModelSerializer):
    """
    序列化用户信息
    """

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'username', 'email', 'phone', 'nickname', 'is_superuser',
            'is_staff',
            'last_login', 'date_joined')
        read_only_fields = (
            'username', 'is_superuser', 'is_staff', 'last_login',
            'date_joined')

        # def update(self, instance, validated_data):


class ProfileApiView(generics.GenericAPIView):
    """
    用户信息接口
    parameters:
    - name: data
      type: json
      required: true
      location: form
    """
    serializer_class = ProfileSerializer
    filter_backends = None
    pagination_class = None

    def get(self, request):
        queryset = User.objects.get(id=request.user.id)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def post(self, request):
        instance = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=instance,
                              validated_data=serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetToken(generics.GenericAPIView):
    """
    获取Token令牌
    """
    queryset = Token.objects.all()
    permission_classes = [DjangoModelPermissions]
    pagination_class = None

    def get(self, request):
        try:
            access_token = self.get_queryset().get(user_id=request.user.id).key
            return Response({'token': access_token})
        except Token.DoesNotExist:
            return Response({})
        except Exception as e:
            return Response({'系统异常: {}'.format(str(e))},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InitToken(generics.GenericAPIView):
    """
    初始化Token令牌
    """
    queryset = Token.objects.all()
    pagination_class = None
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        try:
            if len(Token.objects.filter(user_id=request.user.id)) > 0:
                item = Token.objects.get(user_id=request.user.id)
                item.delete()
            new_item = Token.objects.create(user_id=request.user.id)
            new_item.save()
            return Response({'token': new_item.key})
        except Exception as e:
            return Response({'系统异常: {}'.format(str(e))},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
