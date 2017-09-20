# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Employee, Appraisal, Competencies
from django.contrib import admin

admin.site.register(Employee)
admin.site.register(Appraisal)
admin.site.register(Competencies)

# Register your models here.
