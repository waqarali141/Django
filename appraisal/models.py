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
    feedback_completed = models.BooleanField(default=False)

    @property
    def all_reportee(self):
        return self.employee_set.all()

    def set_feedback(self):
        if self.employee_set.all():
            completed = True
            for employee in self.employee_set.all():
                if not employee.receiver:
                    completed = False
                    break
            self.feedback_completed = completed


class Appraisal(models.Model):
    comment = models.TextField()
    year = models.CharField(max_length=4)
    score = models.IntegerField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver',
                                    null=True, blank=True)
    from_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='giver',
                                      null=True, blank=True)


class Competencies(models.Model):
    def __str__(self):
        return self.name
    competency_type = (('py', 'Python'),
                       ('tw', 'Team Work'),
                       ('dj', 'Django'),
                       ('cm', 'Communication'),
                       )
    name = models.CharField(max_length=35, choices=competency_type)
    score = models.IntegerField()
    appraisal = models.ForeignKey(Appraisal, on_delete=models.CASCADE,
                                      null=True, blank=True)