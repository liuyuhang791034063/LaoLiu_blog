from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.views.generic import TemplateView,ListView,CreateView,DeleteView
from django.views.generic.base import TemplateResponseMixin,View
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Course,Lesson
from .forms import CreateCourseForm,CreateLessonForm
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

def Delete(request,id):
    try:
        courses = Course.objects.filter(id = id)
        courses.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("0")

class CreateLessonView(LoginRequiredMixin,View):
    model = Lesson
    login_url = '/account/login/'

    def get(self, request, *args, **kwargs):
        form = CreateLessonForm(user=self.request.user) # 这里因为表单模型中重写了__init__,所以实例化时需要传入user
        # form = CreateLessonForm()
        return render(request, "course/manage/create_lesson.html", {"form":form})

    def post(self, request, *args, **kwargs):
        form = CreateLessonForm(self.request.user, request.POST, request.FILES) #因为传入表单中有文件,所以必须传入FILES
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.user = self.request.user
            new_lesson.save()
            return redirect("course:manage_course") #返回软链接
class ListLessonsView(LoginRequiredMixin,TemplateResponseMixin, View):
    login_url = '/accout/login/'
    template_name = 'course/manage/list_lessons.html'

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        return self.render_to_response({'course':course}) #传递数据到前端模板

class Redit_CourseView(LoginRequiredMixin,View):
    model = Course
    login_url = '/account/login/'

    def get(self, request, course_id, *args, **kwargs):
        return render(request, 'course/manage/redit_course.html')

    def post(self, request, course_id, *args, **kwargs):
        redit_course = get_object_or_404(Course,id=course_id)
        try:
            redit_course.title = request.POST['title']
            redit_course.overview = request.POST['overview']
            redit_course.save()
            return redirect("course:manage_course")
        except:
            print("sorre")
            return

class DetailLessonView(LoginRequiredMixin, TemplateResponseMixin, View):
    login_url = '/account/login/'
    template_name = "course/manage/detail_lesson.html"

    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return self.render_to_response({"lesson":lesson})

class StudentListLessonView(ListLessonsView):
    template_name = "course/slist_lessons.html"

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        is_learned = '0'
        for a in course.student.all():
            if request.user.username == a.username:
                is_learned = '1'
        return self.render_to_response({'course':course,'learned_flag':is_learned})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(id = kwargs['course_id'])
        course.student.add(self.request.user)
        return HttpResponse("ok")
