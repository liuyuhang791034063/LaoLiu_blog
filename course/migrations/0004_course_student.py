# Generated by Django 2.0.4 on 2018-05-17 11:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_auto_20180517_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]