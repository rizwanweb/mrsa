from django.db import models

# Create your models here.


class Port(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)
    address = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.shortname


class Terminal(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)
    licenseNumber = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.shortname
