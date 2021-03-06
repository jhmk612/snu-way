# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 06:11
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_remove_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=models.DecimalField(decimal_places=2, help_text='5점 만점', max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
