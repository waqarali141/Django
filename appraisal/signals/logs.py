import logging

from django.utils import timezone

from appraisal.models import Log

logger = logging.getLogger(__name__)


def log_feedback(sender, **kwargs):
    obj, created = Log.objects.get_or_create(
        date=timezone.now(),
        feedback=kwargs['instance'],
    )
    if created:
        obj.save()
    logger.info("{}".format(obj.log()))
