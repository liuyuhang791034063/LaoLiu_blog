# Generated by Django 2.0.2 on 2018-04-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogarticles',
            old_name='auther',
            new_name='author',
        ),
    ]
