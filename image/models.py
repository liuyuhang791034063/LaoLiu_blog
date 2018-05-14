from django.db import models
from django.contrib.auth.models import User

from slugify import slugify

class Image(models.Model):
    user = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE) #on_delete 外键删除模式 CASCADE默认选项 PROTECT 保护选项 删除时会弹出protected错误
    title = models.CharField(max_length=300)
    url = models.URLField()
    slug = models.SlugField(max_length=500, blank=True) # slug可以格式化url，也可以把转化中文为英文格式
    description = models.TextField(blank=True)
    created = models.DateField(auto_now=True, db_index=True) # db_index 说明数据库拿这个当做索引
    image = models.ImageField(upload_to='images/%Y/%m/%d') #upload_to 规定了图片上传的存储路径

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image,self).save(*args,**kwargs)

