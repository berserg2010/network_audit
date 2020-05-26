from django.db import models


class Workstation(models.Model):

    ip_address = models.GenericIPAddressField(
        primary_key=True,
    )

    is_active = models.BooleanField(default=True, null=False, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ip_address']
