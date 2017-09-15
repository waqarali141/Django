__author__ = 'waqarali'

from django.forms import ModelForm
from .models import Appraisal, Competencies


class CompetencyForm(ModelForm):
    class Meta:
        model = Competencies
        fields = ['name', 'score']


class AppraisalForm(ModelForm):
    class Meta:
        model = Appraisal
        fields = ['comment', 'year']