from django.db import models

from .common import BaseModel

class BaseBoard(BaseModel):

    _wmi_object = "Win32_BaseBoard"

    Description = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Product = models.CharField(max_length=255)
    SerialNumber = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Tag = models.CharField(max_length=255)
    Version = models.CharField(max_length=255)

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"

