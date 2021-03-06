# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 13:02
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='latlng',
            field=models.CharField(default='37.4624015, 126.9520365', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(auto_now_add=True),
        ),
    ]
