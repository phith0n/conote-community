# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 20:46
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


def add_drop(apps, schema_editor):
    User = apps.get_model("ucenter", "User")
    for user in User.objects.all():
        user.option['drop'] = 'robots.txt|favicon.ico'
        user.save()


def drop_drop(apps, schema_editor):
    User = apps.get_model("ucenter", "User")
    for user in User.objects.all():
        del user.option['drop']
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ucenter', '0006_user_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='option',
            field=jsonfield.fields.JSONField(default={'drop': 'robots.txt|favicon.ico', 'filter': None, 'ignore_note': True}, verbose_name='设置'),
        ),
        migrations.RunPython(code=add_drop, reverse_code=drop_drop)
    ]
