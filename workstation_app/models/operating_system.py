from django.db import models

from .common import BaseModel


class OperatingSystem(BaseModel):

    _wmi_object = "Win32_OperatingSystem"

    BootDevice = models.CharField(max_length=255, null=True, blank=True, default='')
    BuildNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    Caption = models.CharField(max_length=255, null=True, blank=True, default='')
    CodeSet = models.CharField(max_length=255, null=True, blank=True, default='')
    CountryCode = models.CharField(max_length=255, null=True, blank=True, default='')
    CSName = models.CharField(max_length=255, null=True, blank=True, default='')
    Locale = models.CharField(max_length=255, null=True, blank=True, default='')
    Manufacturer = models.CharField(max_length=255, null=True, blank=True, default='')
    OSArchitecture = models.CharField(max_length=255, null=True, blank=True, default='')
    RegisteredUser = models.CharField(max_length=255, null=True, blank=True, default='')
    SerialNumber = models.CharField(max_length=255, null=True, blank=True, default='')
    Status = models.CharField(max_length=255, null=True, blank=True, default='')
    Version = models.CharField(max_length=255, null=True, blank=True, default='')

    CurrentTimeZone = models.SmallIntegerField(null=True, blank=True, default=None)

    ServicePackMajorVersion = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    ServicePackMinorVersion = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    EncryptionLevel = models.PositiveIntegerField(null=True, blank=True, default=None)
    NumberOfUsers = models.PositiveIntegerField(null=True, blank=True, default=None)
    OSLanguage = models.PositiveIntegerField(null=True, blank=True, default=None)
    OSProductSuite = models.PositiveIntegerField(null=True, blank=True, default=None)

    # Datetime
    InstallDate = models.CharField(max_length=255, null=True, blank=True, default='')
    LastBootUpTime = models.CharField(max_length=255, null=True, blank=True, default='')
    LocalDateTime = models.CharField(max_length=255, null=True, blank=True, default='')

    def __str__(self):
        return f"<{self.__class__} {self.Caption}>"
