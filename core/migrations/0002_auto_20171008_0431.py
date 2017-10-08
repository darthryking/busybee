# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]
