# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-03 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0019_dnslog_ip_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='language',
            field=models.CharField(blank=True, choices=[('clike', 'C/C++/C#'), ('go', 'GO'), ('htmlembedded', 'HTML'), ('http', 'HTTP'), ('java', 'Java'), ('javascript', 'Javascript'), ('lua', 'Lua'), ('nginx', 'Nginx'), ('perl', 'Perl'), ('php', 'PHP'), ('powershell', 'PowerShell'), ('python', 'Python'), ('ruby', 'Ruby'), ('rust', 'Rust'), ('shell', 'shell'), ('sql', 'SQL'), ('swift', 'Swift'), ('vbscript', 'VBScript'), ('vue', 'Vue'), ('xml', 'XML'), ('yaml', 'YAML'), ('css', 'CSS')], max_length=32, null=True, verbose_name='代码语言'),
        ),
    ]
