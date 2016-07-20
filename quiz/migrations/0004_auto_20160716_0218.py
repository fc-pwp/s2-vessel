# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20160706_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='number',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question/%Y/%m/%d'),
        ),
    ]