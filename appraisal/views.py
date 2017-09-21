# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .forms import CompetencyModelForm, AppraisalModelForm
from .models import Employee, Competencies, Appraisal


class FormContext(object):
    competency_form = CompetencyModelForm()
    appraisal = AppraisalModelForm()
    competency = Competencies()
    appraisal_form = inlineformset_factory(Appraisal, Competencies, extra=4,
                                           fields=('name', 'score'))
    form = appraisal_form()
    extra_context = {'form': {'appraisal_form': appraisal,
                              'competency_form': form}}

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
        if self.request.user.employee.type == 'mg':
            notifications = list()
            for reportee in self.request.user.employee.all_reportee:
                if reportee.feedback_completed:
                    notifications.append({'employee': reportee})
            context.update({'notifications': notifications})
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


class AddAppraisal(LoginRequiredMixin, CreateView):
    model = Appraisal
    fields = ['comment', 'year']

    def form_valid(self, form):

        from_employee = self.request.user.employee
        to_employee = Employee.objects.get(pk=self.kwargs['pk'])

        if to_employee in from_employee.all_reportee:
            form.instance.from_employee = from_employee
            form.instance.to_employee = to_employee

            form.instance.score = 0
            recieved = form.save()

            appraisal_form = inlineformset_factory(Appraisal, Competencies,
                                                   fields=('name', 'score'))
            formset = appraisal_form(self.request.POST, instance=recieved)

            appraisal_score = 0
            for competency in formset.cleaned_data:
                appraisal_score += competency['score']
            recieved.score = appraisal_score / len(formset.cleaned_data)

            recieved.save()
            formset.save()

            self.request.user.employee.set_feedback()
            self.request.user.employee.save()

            self.success_url = reverse('appraisal:detail', args=(self.kwargs['pk'],))
            return super(AddAppraisal, self).form_valid(form)
        else:
            return HttpResponse('Unauthorised', status=401)


class AppraisalDelete(DeleteView):
    model = Appraisal

    def get_success_url(self):
        return reverse('appraisal:detail', args=(self.kwargs['user_id'],))

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        request.user.employee.feedback_completed = False
        request.user.employee.save()

        return HttpResponseRedirect(success_url)

# @login_required(login_url='/appraisal/login')
# def add(request, pk=''):
#     appraisal = AppraisalModelForm(request.POST)
#     from_employee = request.user.employee
#     to_employee = Employee.objects.get(pk=pk)
#     if to_employee in from_employee.all_reportee:
#         appraisal.instance.from_employee = from_employee
#         appraisal.instance.to_employee = to_employee
#         recieved = appraisal.save()
#         appraisal_form = inlineformset_factory(Appraisal, Competencies,
#                                                fields=('name', 'score'))
#         formset = appraisal_form(request.POST, instance=recieved)
#         appraisal_score = 0
#         for competency in formset.cleaned_data:
#             appraisal_score += competency['score']
#         recieved.score = appraisal_score / len(formset.cleaned_data)
#         recieved.save()
#         formset.save()
#         request.user.employee.set_feedback()
#         request.user.employee.save()
#         # print request.user.employee.feedback_completed
#         return HttpResponseRedirect(reverse('appraisal:detail', args=(pk,)))
#
#     else:
#         return HttpResponse('Unauthorised', status=401)
