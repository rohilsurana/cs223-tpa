# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=2),
        ),
    ]