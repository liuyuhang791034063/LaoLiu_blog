#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-15 下午7:25
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from django.views.generic import TemplateView
from .views import AboutView,CourseListView,ManageCourseListView,CreatedCourseView,DeleteCourseView,CreateLessonView,ListLessonsView
from .views import Redit_CourseView,DetailLessonView,StudentListLessonView

urlpatterns = [
    # url(r'about/$', TemplateView.as_view(template_name="course/about.html")), # 使用类视图，方法一，不需要写视图函数
    url(r'about/$', AboutView.as_view(), name='about'),  # 方法二，写一个继承TemplateView的新类
    url(r'course-list/$',CourseListView.as_view(), name='course_list'),
    url(r'manage-course/$', ManageCourseListView.as_view(), name='manage_course'),
    url(r'create-course/$', CreatedCourseView.as_view(), name='create_course'),
    url(r'delete-course/(?P<pk>\d+)/$',DeleteCourseView.as_view(), name='delete_course'),
    url(r'create-lesson/$', CreateLessonView.as_view(), name='create_lesson'),
    url(r'list-lessons/(?P<course_id>\d+)/$',ListLessonsView.as_view(), name='list_lessons'),
    url(r'redit-course/(?P<course_id>\d+)/$',Redit_CourseView.as_view(), name='redit_course'),
    url(r'detail-lesson/(?P<lesson_id>\d+)/$',DetailLessonView.as_view(), name='detail_lesson'),
    url(r'lessons-list/(?P<course_id>\d+)/$', StudentListLessonView.as_view(), name='lessons_list'),
]