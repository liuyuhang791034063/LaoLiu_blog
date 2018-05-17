#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-16 下午4:26
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Course,Lesson

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title","overview")


class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course','title','video','description','attach']
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(user=user)