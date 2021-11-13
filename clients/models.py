from django.db import models

# Create your models here.

class Client(models.Model):

    name = models.CharField(unique=True, max_length=200)
    person = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    address2 = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    NTN = models.CharField(max_length=20)
    GST = models.CharField(max_length=20)
    director = models.CharField(max_length=100, null=True, blank=True)
    nic = models.CharField(max_length=20, null=True, blank=True)




    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
