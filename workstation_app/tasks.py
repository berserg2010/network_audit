from __future__ import absolute_import, unicode_literals
import functools
from typing import Tuple

from django.core.cache import cache
from django.apps import apps
import requests
from celery import shared_task, group, signals, chord
import os

from .models import *
from utils.connector import connector
from .models import Workstation
from network_audit import settings


@signals.beat_init.connect
def task_adding_workstation_ip_address_to_the_cache_at_startup(sender=None, headers=None, body=None, **kwargs):

    workstations_ip_addresses = list(Workstation.objects.filter(is_active=True).values_list('ip_address', flat=True))

    cache.set("workstations_ip_addresses", workstations_ip_addresses, timeout=None)
    cache.set("WINRM_USERNAME", settings.WINRM_USERNAME, timeout=None)
    cache.set("WINRM_PASSWORD", settings.WINRM_PASSWORD, timeout=None)


@shared_task
def task_get_data_from_workstations():

    ip_addresses = cache.get("workstations_ip_addresses")

    data = group(
        task_get_wmi_objects.s(ip_address) for ip_address in ip_addresses
    ).apply_async()

    return None


@shared_task
def task_get_wmi_objects(ip_address: str):

    data = (
        group(task_get_wmi_object.s(ip_address, wmi_class) |
        task_entering_data_into_the_wmi_model.s() for wmi_class in list_models)
    ).apply_async()

    return None


@shared_task
@connector
def task_get_wmi_object(**kwargs):
    return kwargs


@shared_task
def task_entering_data_into_the_wmi_model(data: dict):

    ip_address = data.get("ip_address")
    wmi_class = data.get("wmi_class")
    std_out = data.get("std_out")

    workstation_instance = Workstation.objects.get(pk=ip_address)

    print(workstation_instance)

    wmi_model = apps.get_model(app_label=f"workstation_app.{wmi_class}")

    if isinstance(std_out, list):
        for item in std_out:
            wmi_instance = wmi_model(workstation=workstation_instance)
            get_property_in_wmi_instance(wmi_instance, item).save()

    else:
        wmi_instance = wmi_model(workstation=workstation_instance)
        get_property_in_wmi_instance(wmi_instance, std_out).save()


def get_property_in_wmi_instance(wmi_instance, properties: dict):

    for key, value in properties.items():
        setattr(wmi_instance, key, value)

    return wmi_instance

