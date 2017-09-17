__author__ = 'waqarali'

from django.forms import ModelForm
from .models import Appraisal, Competencies
from django.forms import inlineformset_factory
from django import forms


class CompetencyModelForm(ModelForm):
    class Meta:
        model = Competencies
        fields = ['name', 'score']


class AppraisalModelForm(ModelForm):
    class Meta:
        model = Appraisal
        fields = ['comment', 'year']
