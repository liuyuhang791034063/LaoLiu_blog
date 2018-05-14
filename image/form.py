#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午1:27
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : form.py
# @Software: PyCharm

from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from urllib import request

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')

    def clean_url(self): #处理某个字段的函数 构造 clean+字段名称
        url = self.cleaned_data['url'] # 获取字段需要从self.clearn_data中获取
        valid_extensions = ['jpg','jpeg','png'] # 规定了文件后缀
        extension = url.rsplit('.',1)[1].lower() # 从文件名中分解出后缀名
        if extension not in valid_extensions:
            raise forms.ValidationError("The given Url does not match valid image extension.")
        return url
    def save(self,force_insert=False ,commit=True, force_update=False):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{0}.{1}'.format(slugify(image.title),image_url.rsplit('.',1)[1].lower())
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()

        return image