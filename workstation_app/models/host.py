from django.db import models


class Host(models.Model):

    ip_address = models.GenericIPAddressField(
        primary_key=True,
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ip_address']
