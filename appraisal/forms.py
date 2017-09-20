# -*- coding: utf-8 -*-
__author__ = 'waqarali'

from django.forms import ModelForm

from .models import Appraisal, Competencies


class CompetencyModelForm(ModelForm):
    class Meta:
        model = Competencies
        fields = ['name', 'score']


class AppraisalModelForm(ModelForm):
    class Meta:
        model = Appraisal
        fields = ['comment', 'year']
