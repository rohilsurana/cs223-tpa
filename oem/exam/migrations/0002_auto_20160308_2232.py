# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testresult',
            unique_together=set([('student', 'test')]),
        ),
    ]
