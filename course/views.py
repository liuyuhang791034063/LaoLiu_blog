from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from .models import Course

class AboutView(TemplateView):
    template_name = 'course/about.html'

class CourseListView(ListView):
    model = Course # 可获取相应模型的数据库表
    context_object_name = "courses" # 模板变量名称
    template_name = 'course/course_list.hmtl' 