from __future__ import absolute_import, unicode_literals
from django.core.cache import cache
import requests
from celery import shared_task, group, signals

from .models import *
from utils.connector import connector
from .models import Host
from network_audit import settings


# @signals.beat_init.connect
# def task_adding_hosts_ip_address_to_the_cache_at_startup(sender=None, headers=None, body=None, **kwargs):
#     ip_address_id = list(Host.objects.all().values_list('ip_address_id', flat=True))
#     cache.set('hosts_ip_address', ip_address_id, timeout=None)
#
#
# @shared_task
# def get_wmi_objects_and_save_in_db():
#     hosts_ip_address = cache.get('hosts_ip_address')
#     return (
#         group(
#             task_get_wmi_objects.s(ip_address) for ip_address in hosts_ip_address
#         ) |
#             task_entering_data_into_the_wmi_model.s()
#     ).apply_async()


@shared_task
def task_get_wmi_objects(ip_address):
    data = group(
        task_get_wmi_object.s(ip_address, wmi_class) for wmi_class in list_models
    ).apply_async()
    return data

@shared_task
@connector
def task_get_wmi_object(**kwargs):
    return kwargs.get("data")


@shared_task
def task_entering_data_into_the_wmi_model():
    pass
