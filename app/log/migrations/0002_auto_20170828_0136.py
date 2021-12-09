# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='raw',
            field=models.TextField(blank=True, null=True, verbose_name='原始记录'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='referrer',
            field=models.TextField(blank=True, null=True, verbose_name='来源网址'),
        ),
    ]
