from django.db import models

from .workstation import Workstation


class BaseModel(models.Model):

    _wmi_object : str

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    workstation = models.ForeignKey(
        'Workstation',
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True
        ordering = ["created", "updated"]
