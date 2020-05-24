from django.core.handlers.wsgi import WSGIRequest
from django.apps import apps
from django.shortcuts import render
import functools

from workstation_app.models import *

def get_wim_object_with_properties(wmi_class: str) -> str:

    get_model = apps.get_model(app_label=f"workstation_app.{wmi_class}")

    list_properties = tuple(filter(lambda i: i[0].isupper(), dir(get_model)))

    return compare_command(
        get_wmi_object(getattr(get_model, "_wmi_object")),
        select_object(list_properties)
    )


def get_wmi_object(wmi_class: str) -> str:
    return f"Get-WmiObject -Class {wmi_class}"


def select_object(prop: tuple) -> str:
    return f"Select-Object -Property {', '.join(prop)}"


ConvertToJson = 'ConvertTo-Json -Compress'


def compare_command(*args: str) -> str:
    return f"{' | '.join(args)}"


def render_item(func):
    @functools.wraps(func)
    def wrapped(request: WSGIRequest, **kwargs: dict):

        data = kwargs.get('data')
        data_to_list = data if isinstance(data, list) else [data]

        return func(render(
            request,
            "workstation_app/item.html",
            {'data': data_to_list, "error": kwargs.get('error')}
        ))
    return wrapped
