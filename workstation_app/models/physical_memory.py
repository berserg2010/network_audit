from django.db import models

from .common import BaseModel


class PhysicalMemory(BaseModel):

    _wmi_object = "Win32_PhysicalMemory"

    BankLabel = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    PartNumber = models.CharField(max_length=255)
    SerialNumber = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)

    DataWidth = models.PositiveSmallIntegerField()
    FormFactor = models.PositiveSmallIntegerField()
    MemoryType = models.PositiveSmallIntegerField()
    TotalWidth = models.PositiveSmallIntegerField()
    TypeDetail = models.PositiveSmallIntegerField()

    PositionInRow = models.PositiveIntegerField()
    Speed = models.PositiveIntegerField()

    Capacity = models.BigIntegerField()

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"


