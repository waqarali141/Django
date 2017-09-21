# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Employee, Appraisal, Competencies


# admin.site.register(Employee)
admin.site.register(Appraisal)
admin.site.register(Competencies)


# Register your models here.


class AdminEmployeeModel(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ['name']


admin.site.register(Employee, AdminEmployeeModel)
