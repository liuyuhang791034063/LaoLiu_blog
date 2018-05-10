from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^blog/',include(('blog.urls','blog') , namespace='blog')),
    url(r'^account/', include(('account.urls','account'), namespace = 'account')),
    #url(r'^pwd_reset/', include(('password_reset.urls','pwd_reset') ,namespace='pwd_reset')),
    url(r'^article/', include(('article.urls','article'),namespace= 'article')),
    url(r'^home/', TemplateView.as_view(template_name="home.html"),name="home"),
]
