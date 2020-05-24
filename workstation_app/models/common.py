from django.db import models

from .host import Host


class BaseModel(models.Model):

    _wmi_object : str

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    host = models.ForeignKey(
        'Host',
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True
        ordering = ["created", "updated"]

    # @classmethod
    # def get_wmi_object(cls):
    #     return f"{cls._wmi_object}"
    #
    # def __setitem__(self, key, value):
    #     self.__setattr__(key, value)
    #
    # def __getitem__(self, key):
    #     return self.__getattribute__(key)