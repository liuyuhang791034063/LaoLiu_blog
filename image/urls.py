#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午2:42
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list-images/$',views.list_images, name="list_images"),
    url(r'^upload-image/$', views.upload_image, name="upload_image"),
    url(r'^del-image/$',views.del_image, name="del_image"),
]