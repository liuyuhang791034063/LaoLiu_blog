#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-15 下午7:25
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from django.views.generic import TemplateView
from .views import AboutView,CourseListView,ManageCourseListView,CreatedCourseView,DeleteCourseView,Delete

urlpatterns = [
    # url(r'about/$', TemplateView.as_view(template_name="course/about.html")), # 使用类视图，方法一，不需要写视图函数
    url(r'about/$', AboutView.as_view(), name='about'),  # 方法二，写一个继承TemplateView的新类
    url(r'course-list/$',CourseListView.as_view(), name='course_list'),
    url(r'manage-course/$', ManageCourseListView.as_view(), name='manage_course'),
    url(r'create-course/$', CreatedCourseView.as_view(), name='create_course'),
    url(r'delete-course/(?P<pk>\d+)/$',DeleteCourseView.as_view(), name='delete_course'),

]