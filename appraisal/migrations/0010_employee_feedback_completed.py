# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0009_auto_20170917_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='feedback_completed',
            field=models.BooleanField(default=False),
        ),
    ]
