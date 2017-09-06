# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic


class Index(generic.ListView):
    context_object_name = 'employee_list'
    template_name = 'appraisal/index.html'

    def get_queryset(self):
        return self.request.user.employee.all_reportee

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

