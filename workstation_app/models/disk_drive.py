from django.db import models

from .common import BaseModel


class DiskDrive(BaseModel):

    _wmi_object = "Win32_DiskDrive"

    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    DeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    FirmwareRevision = models.CharField(max_length=255, null=True, blank=True, default='')
    InterfaceType = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    Model = models.CharField(max_length=255, null=True, blank=True, default='')
    SerialNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')
    SystemName = models.CharField(max_length=255, null=True, blank=True, default='')

    BytesPerSector = models.PositiveIntegerField(null=True, blank=True, default=None)
    ConfigManagerErrorCode = models.PositiveIntegerField(null=True, blank=True, default=None)
    Index = models.PositiveIntegerField(null=True, blank=True, default=None)
    Partitions = models.PositiveIntegerField(null=True, blank=True, default=None)
    Signature = models.PositiveIntegerField(null=True, blank=True, default=None)
    TotalHeads = models.PositiveIntegerField(null=True, blank=True, default=None)
    TracksPerCylinders = models.PositiveIntegerField(null=True, blank=True, default=None)

    Size = models.BigIntegerField(null=True, blank=True, default=None)
    TotalCylinders = models.BigIntegerField(null=True, blank=True, default=None)
    TotalSectors = models.BigIntegerField(null=True, blank=True, default=None)
    TotalTracks = models.BigIntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"<{self.__class__} {self.Model} {self.Size / (1024 ** 3)} GB>"
