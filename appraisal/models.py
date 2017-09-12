# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    def __str__(self):
        return self.name

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_type = (('mg', 'Manager'),
                     ('gm', 'General Manager'),
                     ('sf', 'Staff')
                     )

    name = models.CharField(max_length=40)
    type = models.CharField(max_length=2,
                            choices=employee_type,
                            default='sf')
    joined_date = models.DateTimeField('date joined', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    reporting_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def all_reportee(self):
        return self.employee_set.all()


class Appraisal(models.Model):
    comment = models.TextField()
    year = models.CharField(max_length=4)
    score = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver',
                                    null=True, blank=True)
    from_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='giver',
                                      null=True, blank=True)


class Competencies(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=35)
    score = models.IntegerField()
    appraisal = models.ManyToManyField(Appraisal)

