# -*- coding: utf-8 -*-
import logging

from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from appraisal.models import Appraisal

from appraisal.models import Log

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Appraisal)
def log_feedback(sender, **kwargs):
    obj, created = Log.objects.get_or_create(
        date=timezone.now(),
        feedback=kwargs['instance'],
    )
    if created:
        obj.save()
    logger.info("{}".format(obj.log()))
