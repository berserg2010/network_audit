from django.db import models

from .common import BaseModel


class Processor(BaseModel):

    _wmi_object = "Win32_Processor"

    Description = models.CharField(max_length=255)
    DeviceID = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    ProcessorId = models.CharField(max_length=255)
    SocketDesignation = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    SystemName = models.CharField(max_length=255)

    AddressWidth = models.PositiveSmallIntegerField()
    Family = models.PositiveSmallIntegerField()
    Revision = models.PositiveSmallIntegerField()

    MaxClockSpeed = models.PositiveIntegerField()
    NumberOfCores = models.PositiveIntegerField()
    NumberOfLogicalProcessors = models.PositiveIntegerField()

    VirtualizationFirmwareEnabled = models.NullBooleanField()

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
