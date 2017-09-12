# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, User, Competencies


class Index(LoginRequiredMixin, generic.ListView):
    context_object_name = 'employee_list'
    template_name = 'appraisal/index.html'

    def get_queryset(self):
        try:
            return self.request.user.employee.all_reportee
        except:
            return {}

class DetailUserView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    template_name = 'appraisal/detail.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return Employee.objects.filter(pk=self.kwargs['pk'])




# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index