from django.db import models

from .common import BaseModel


class PhysicalMemory(BaseModel):

    _wmi_object = "Win32_PhysicalMemory"

    BankLabel = models.CharField(max_length=255, null=True, blank=True, default='')
    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    PartNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    SerialNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')

    DataWidth = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    FormFactor = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    MemoryType = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    TotalWidth = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    TypeDetail = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    PositionInRow = models.PositiveIntegerField(null=True, blank=True, default=None)
    Speed = models.PositiveIntegerField(null=True, blank=True, default=None)

    Capacity = models.BigIntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
