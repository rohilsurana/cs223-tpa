# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
