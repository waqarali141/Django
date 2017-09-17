# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, User, Competencies, Appraisal
from .forms import CompetencyModelForm, AppraisalModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory, BaseInlineFormSet


class FormContext(object):
    competency_form = CompetencyModelForm()
    appraisal = AppraisalModelForm()
    competency = Competencies()
    appraisal_form = inlineformset_factory(Appraisal, Competencies,
                                           fields=('name', 'score'))
    form = appraisal_form()
    extra_context = {'form': {'appraisal_form': appraisal,
                              'competency_form': form}}
    # extra_context = {'form': form}

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

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return context
        # if self.request.user.type == 'mg':


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


def add(request, pk=''):
    appraisal = AppraisalModelForm(request.POST)
    from_employee = request.user.employee
    to_employee = Employee.objects.get(pk=pk)
    appraisal.instance.from_employee = from_employee
    appraisal.instance.to_employee = to_employee
    recieved = appraisal.save()
    appraisal_form = inlineformset_factory(Appraisal, Competencies,
                                           fields=('name', 'score'))
    formset = appraisal_form(request.POST, instance=recieved)
    formset.save()
    return HttpResponseRedirect(reverse('appraisal:detail', args=(pk,)))



class AddAppraisal(LoginRequiredMixin, CreateView):
    model = Appraisal
    fields = ['comment', 'year']

    def form_valid(self, form):
        form.instance.from_employee = self.request.user.employee
        form.instance.to_employee = Employee.objects.get(pk=self.kwargs['pk'])
        form.instance.score = 0
        appraisal_form = inlineformset_factory(Appraisal, Competencies,
                                               fields=('name', 'score'))
        formset = appraisal_form(self.request.POST, form)
        self.success_url = reverse('appraisal:detail', args=(self.kwargs['pk'],))

        return super(AddAppraisal, self).form_valid(form)



