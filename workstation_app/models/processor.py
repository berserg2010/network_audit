from django.db import models

from .common import BaseModel


class Processor(BaseModel):

    _wmi_object = "Win32_Processor"

    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    DeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    Name = models.CharField(max_length=255, null=True, blank=True, default='')
    ProcessorId = models.CharField(max_length=255, null=True, blank=True, default='')
    SocketDesignation = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')
    SystemName = models.CharField(max_length=255, null=True, blank=True, default='')

    AddressWidth = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    Family = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    Revision = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    MaxClockSpeed = models.PositiveIntegerField(null=True, blank=True, default=None)
    NumberOfCores = models.PositiveIntegerField(null=True, blank=True, default=None)
    NumberOfLogicalProcessors = models.PositiveIntegerField(null=True, blank=True, default=None)

    VirtualizationFirmwareEnabled = models.NullBooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
