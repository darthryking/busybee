# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171008_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default='FF0000', max_length=6),
            preserve_default=False,
        ),
    ]
