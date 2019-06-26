# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]