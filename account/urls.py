from django.conf.urls import  url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^login/$', views.user_login, name="user_login"), #自定义的登陆
    url(r'^login/$', auth_views.login, {"template_name":"account/login.html"}, name="user_login"), #django内置的登陆
    url(r'^logout/$', auth_views.logout, {"template_name":"account/logout.html"}, name="user_logout"),
]