# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0010_note_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblog',
            name='method',
            field=models.TextField(default='GET', verbose_name='方法'),
        ),
    ]
