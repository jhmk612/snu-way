# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-10 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160810_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
