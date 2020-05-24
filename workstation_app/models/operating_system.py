from django.db import models

from .common import BaseModel


class OperatingSystem(BaseModel):

    _wmi_object = "Win32_OperatingSystem"

    BootDevice = models.CharField(max_length=255)
    BuildNumber = models.CharField(max_length=255)
    Caption = models.CharField(max_length=255)
    CodeSet = models.CharField(max_length=255)
    CountryCode = models.CharField(max_length=255)
    CSName = models.CharField(max_length=255)
    Locale = models.CharField(max_length=255)
    Manufacturer = models.CharField(max_length=255)
    OSArchitecture = models.CharField(max_length=255)
    RegisteredUser = models.CharField(max_length=255)
    SerialNumber = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Version = models.CharField(max_length=255)

    CurrentTimeZone = models.SmallIntegerField()

    ServicePackMajorVersion = models.PositiveSmallIntegerField()
    ServicePackMinorVersion = models.PositiveSmallIntegerField()

    EncryptionLevel = models.PositiveIntegerField()
    NumberOfUsers = models.PositiveIntegerField()
    OSLanguage = models.PositiveIntegerField()
    OSProductSuite = models.PositiveIntegerField()

    InstallDate = models.DateTimeField()
    LastBootUpTime = models.DateTimeField()
    LocalDateTime = models.DateTimeField()

    def __str__(self):
        return f"<{self.__class__} {self.Caption}>"
