from django.db import models

from .common import BaseModel


class VideoController(BaseModel):

    _wmi_object = "Win32_VideoController"

    Description = models.CharField(max_length=255, null=True, blank=True, default='')
    DeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    DriverVersion = models.CharField(max_length=255, null=True, blank=True, default='')
    InfFilename = models.CharField(max_length=255, null=True, blank=True, default='')
    InstalledDisplayDrivers = models.CharField(max_length=4095, null=True, blank=True, default='')
    PNPDeviceID = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')
    SystemName = models.CharField(max_length=255, null=True, blank=True, default='')
    VideoProcessor = models.CharField(max_length=255, null=True, blank=True, default='')

    Availability = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    VideoArchitecture = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    VideoMemoryType = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    ConfigManagerErrorCode = models.PositiveIntegerField(null=True, blank=True, default=None)
    CurrentBitsPerPixel = models.PositiveIntegerField(null=True, blank=True, default=None)
    CurrentHorizontalResolution = models.PositiveIntegerField(null=True, blank=True, default=None)
    CurrentRefreshRate = models.PositiveIntegerField(null=True, blank=True, default=None)
    CurrentVerticalResolution = models.PositiveIntegerField(null=True, blank=True, default=None)
    MaxRefreshRate = models.PositiveIntegerField(null=True, blank=True, default=None)
    MinRefreshRate = models.PositiveIntegerField(null=True, blank=True, default=None)

    CurrentNumberOfColors = models.BigIntegerField(null=True, blank=True, default=None)
    AdapterRAM = models.BigIntegerField(null=True, blank=True, default=None)

    def __str__(self):
         return f"<{self.__class__} {self.Description}>"
