# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AppraisalConfig(AppConfig):
    name = 'appraisal'

    def ready(self):

        from appraisal.models import Appraisal
        from django.db.models.signals import post_save
        from signals.logs import log_feedback

        post_save.connect(log_feedback, sender=Appraisal, dispatch_uid=Appraisal.id)

