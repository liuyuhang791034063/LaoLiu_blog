from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User
# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="blog_posts",on_delete = models.CASCADE) #如果使用外键，需要添加on_delete属性
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

