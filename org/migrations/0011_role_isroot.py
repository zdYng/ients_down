# Generated by Django 2.0 on 2018-01-19 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0010_remove_role_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='isRoot',
            field=models.BooleanField(default=False, verbose_name='是否为站点管理员'),
        ),
    ]
