from django.db import models

from .common import BaseModel


class VideoController(BaseModel):

    _wmi_object = "Win32_VideoController"

    Description = models.CharField(max_length=255)
    DeviceID = models.CharField(max_length=255)
    DriverVersion = models.CharField(max_length=255)
    InfFilename = models.CharField(max_length=255)
    InstalledDisplayDrivers = models.CharField(max_length=255)
    PNPDeviceID = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    SystemName = models.CharField(max_length=255)
    VideoProcessor = models.CharField(max_length=255)

    Availability = models.PositiveSmallIntegerField()
    VideoArchitecture = models.PositiveSmallIntegerField()
    VideoMemoryType = models.PositiveSmallIntegerField()

    AdapterRAM = models.PositiveIntegerField()
    ConfigManagerErrorCode = models.PositiveIntegerField()
    CurrentBitsPerPixel = models.PositiveIntegerField()
    CurrentHorizontalResolution = models.PositiveIntegerField()
    CurrentRefreshRate = models.PositiveIntegerField()
    CurrentVerticalResolution = models.PositiveIntegerField()
    MaxRefreshRate = models.PositiveIntegerField()
    MinRefreshRate = models.PositiveIntegerField()

    CurrentNumberOfColors = models.BigIntegerField()

    def __str__(self):
         return f"<{self.__class__} {self.Description}>"

