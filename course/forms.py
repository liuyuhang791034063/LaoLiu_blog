#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-16 下午4:26
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Course

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","overview")