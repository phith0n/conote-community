# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-08 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victim',
            name='cookie',
        ),
        migrations.RemoveField(
            model_name='victim',
            name='user_agent',
        ),
    ]
