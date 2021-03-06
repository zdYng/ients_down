# Generated by Django 2.0 on 2018-01-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0015_merge_20180122_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['Company'], 'verbose_name': '部门', 'verbose_name_plural': '部门汇总'},
        ),
        migrations.AlterModelOptions(
            name='department_con',
            options={'ordering': ['Head'], 'verbose_name': '组织架构', 'verbose_name_plural': '组织架构汇总'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['Company']},
        ),
        migrations.AlterModelOptions(
            name='user_con_role',
            options={'ordering': ['Role__Company']},
        ),
    ]
