from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import TemplateView,ListView,CreateView,DeleteView
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Course
from .forms import CreateCourseForm
import json

class UserMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = '/accout/login/' #如果未登录，设置跳转页面

class ManageCourseListView(UserCourseMixin,ListView): #多重继承
    context_object_name = "courses"
    template_name = 'course/manage/manage_course_list.html'

class AboutView(TemplateView):
    template_name = 'course/about.html'

class CourseListView(ListView):
    model = Course # 可获取相应模型的数据库表 获取全部课程 相当于Course.objects.all()
    # queryset = Course.objects.filter(user=User.objects.filter(username="admin")) #寻找特定讲师的课程
    context_object_name = "courses" # 传入模板变量名称
    template_name = 'course/course_list.html'

    # 这是另一种筛选的方法,通过改写get_queryset方法来获取
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(user=User.objects.filter(username="admin"))

class CreatedCourseView(UserCourseMixin, CreateView):
    fields = ['title','overview']
    template_name = 'course/manage/create_course.html'

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect("course:manage_course")
        return self.render_to_response({"form":form})

class DeleteCourseView(UserCourseMixin,DeleteView):
    template_name = 'course/manage/delete_course_confirm.html'
    success_url = reverse_lazy('course:manage_course') #使用反向解析url函数获取url

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args,**kwargs)
        if self.request.is_ajax():
            response_data = {"result":"ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return resp

def Delete(request):
    try:
        courses = Course.objects.filter(id = request.POST['id'])
        courses.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("0")