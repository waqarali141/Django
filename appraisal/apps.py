# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AppraisalConfig(AppConfig):
    name = 'appraisal'

    def ready(self):
        from appraisal.signals.logs import log_feedback
