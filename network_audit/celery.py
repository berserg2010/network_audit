from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

from network_audit import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_audit.settings')

app = Celery('network_audit_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'workstation_app.tasks.task_get_wmi_objects',
        'schedule': 30.0,
        "kwargs": {"ip_address": settings.WINRM_CLIENT_IP},
        # 'schedule': crontab(hour=7),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
