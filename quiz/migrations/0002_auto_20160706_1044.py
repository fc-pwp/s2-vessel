# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]