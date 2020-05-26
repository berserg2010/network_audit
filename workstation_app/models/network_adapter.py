from django.db import models

from .common import BaseModel


class NetworkAdapter(BaseModel):

    _wmi_object = "Win32_NetworkAdapter"

    AdapterType = models.CharField(max_length=255, null=True, blank=True, default='')
    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    DeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    MACAddress = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    Name = models.CharField(max_length=255, null=True, blank=True, default='')
    PNPDeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    ServiceName = models.CharField(max_length=255, null=True, blank=True, default='')
    SystemName = models.CharField(max_length=255, null=True, blank=True, default='')

    Availability = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    InterfaceIndex = models.PositiveIntegerField(null=True, blank=True, default=None)

    Speed = models.BigIntegerField(null=True, blank=True, default=None)

    PhysicalAdapter = models.NullBooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
