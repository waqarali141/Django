# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, User, Competencies, Appraisal
from .forms import AppraisalForm, CompetencyForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse



class FormContext(object):
    appraisal_form = AppraisalForm()
    competency_form = CompetencyForm()
    extra_context = {'form': {'appraisal_form': appraisal_form,
                              'competency_form': competency_form}}

    def get_context_data(self, **kwargs):
        context = super(FormContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class Index(LoginRequiredMixin, generic.ListView):
    context_object_name = 'employee_list'
    template_name = 'appraisal/index.html'

    def get_queryset(self):
        try:
            return self.request.user.employee.all_reportee
        except:
            return {}



class DetailUserView(LoginRequiredMixin, FormContext, generic.DetailView):
    model = Employee
    template_name = 'appraisal/detail.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return Employee.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DetailUserView, self).get_context_data(**kwargs)
        under_employee = {'reporting_employee': self.request.user.employee.all_reportee}
        context.update(under_employee)
        return context

def feedback(request, pk):
    appraisal = AppraisalForm(request.POST)
    print pk
    return


class AddAppraisal(LoginRequiredMixin, CreateView):

    model = Appraisal
    fields = ['comment', 'year']

    def form_valid(self, form):
        form.instance.from_employee = self.request.user.employee
        form.instance.to_employee = Employee.objects.get(pk=self.kwargs['pk'])
        form.instance.score = 0
        self.success_url = reverse('appraisal:detail', args=(self.kwargs['pk'],))
        return super(AddAppraisal, self).form_valid(form)

