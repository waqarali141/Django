# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0010_employee_feedback_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Feedback given')),
                ('feedback', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appraisal.Appraisal')),
            ],
        ),
    ]