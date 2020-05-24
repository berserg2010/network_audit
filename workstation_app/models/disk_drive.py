from django.db import models

from .common import BaseModel


class DiskDrive(BaseModel):

    _wmi_object = "Win32_DiskDrive"

    Description = models.CharField(max_length=255)
    DeviceID = models.CharField(max_length=255)
    FirmwareRevision = models.CharField(max_length=255)
    InterfaceType = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    SerialNumber = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    SystemName = models.CharField(max_length=255)

    BytesPerSector = models.PositiveIntegerField()
    ConfigManagerErrorCode = models.PositiveIntegerField()
    Index = models.PositiveIntegerField()
    Partitions = models.PositiveIntegerField()
    Signature = models.PositiveIntegerField()
    TotalHeads = models.PositiveIntegerField()
    TracksPerCylinders = models.PositiveIntegerField()

    Size = models.BigIntegerField()
    TotalCylinders = models.BigIntegerField()
    TotalSectors = models.BigIntegerField()
    TotalTracks = models.BigIntegerField()

    def __str__(self):
        return f"<{self.__class__} {self.Model} {self.Size / (1024 ** 3)} GB>"
