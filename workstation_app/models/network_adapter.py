from django.db import models

from .common import BaseModel


class NetworkAdapter(BaseModel):

    _wmi_object = "Win32_NetworkAdapter"

    AdapterType = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    DeviceID = models.CharField(max_length=255)
    MACAddress = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    PNPDeviceID = models.CharField(max_length=255)
    ServiceName = models.CharField(max_length=255)
    SystemName = models.CharField(max_length=255)

    Availability = models.PositiveSmallIntegerField()

    InterfaceIndex = models.PositiveIntegerField()

    Speed = models.BigIntegerField()

    PhysicalAdapter = models.NullBooleanField()

    def __str__(self):
        return f"<{self.__class__} {self.Description}>"
