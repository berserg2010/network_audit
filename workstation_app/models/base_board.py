from django.db import models

from .common import BaseModel

class BaseBoard(BaseModel):

    _wmi_object = "Win32_BaseBoard"

    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    Product = models.CharField(max_length=255, null=True, blank=True, default='')
    SerialNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')
    Tag = models.CharField(max_length=255, null=True, blank=True, default='')
    Version = models.CharField(max_length=255, null=True, blank=True, default='')

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
