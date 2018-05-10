#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-6 下午1:51
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import ArticleColumn,ArticlePost,Comment,ArticleTag

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title","body")
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator","body",)

class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ("tag",)