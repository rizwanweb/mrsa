import math
from django.db import models
from django.db.models import Sum

from base.models import Port, Terminal
#from bl.models import BL
from clients.models import Client
from item.models import Item
# Create your models here.
GD_TYPE = [
    ('IB', 'INTO BOND'),
    ('EB', 'EX BOND'),
    ('ST', 'SAFE TRANSPORTAION'),
    ('HC', 'HOME CONSUMPTION'),
]


class LC(models.Model):
    gdType = models.CharField(max_length=20, choices=GD_TYPE, default='IB')
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    lcNo = models.CharField(max_length=100)
    lcDate = models.DateField()
    totalQuantity = models.FloatField()
    vessel = models.CharField(max_length=100)
    igm = models.IntegerField()
    igmDate = models.DateField()
    totalBL = models.IntegerField()
    dv = models.FloatField()
    av = models.FloatField()
    exRate = models.FloatField()
    insurance = models.FloatField()
    pqaRate = models.FloatField(default=31)
    fed = models.FloatField(default=13)
    pqaCharges = models.FloatField(null=True, blank=True)

    billed = models.BooleanField(default=False)
    psqc = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        quantity = math.ceil(self.totalQuantity)
        pcharges = quantity * self.pqaRate
        pcharges += pcharges * self.fed
        self.pqaCharges = round(pcharges)
        super().save(*args, **kwargs)

    # def get_sum_of_bl(self):
    #    return BL.objects.filter(lc=self).aggregate(Sum('importValuePKR'))['bl__sum']

    def __str__(self):
        return self.vessel + "--IGM -" + str(self.igm) + "--LC# -" + self.lcNo
