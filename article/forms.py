#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-6 下午1:51
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import ArticleColumn

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)