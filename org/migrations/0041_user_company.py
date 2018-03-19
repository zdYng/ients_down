# Generated by Django 2.0 on 2018-02-27 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0040_role_con_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='org.Company', verbose_name='公司'),
        ),
    ]