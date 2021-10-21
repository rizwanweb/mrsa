from django.db import models
import math
from base.models import Terminal
from lc.models import LC

# Create your models here.

class BL(models.Model):
    lc = models.ForeignKey(LC, on_delete=models.CASCADE)
    blNo = models.CharField(max_length=100)
    blDate = models.DateField(auto_now=False, auto_now_add=False)
    index = models.IntegerField()
    quantity = models.FloatField()
    insurance = models.FloatField(blank=True)
    usd = models.FloatField(blank=True)
    landingCharges = models.FloatField(blank=True)
    importValuePKR = models.FloatField(blank=True)
    whRate = models.FloatField(default=0.25)
    warehousingCharges = models.FloatField(blank=True)
    exciseRate = models.FloatField(default=1.25)
    excise = models.FloatField(blank=True)
    stampCharges = models.FloatField(blank=True)

    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE, null=True, blank=True)
    isTerminal = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        self.insurance = round((self.lc.insurance / self.lc.totalQuantity) * self.quantity)
        if self.lc.dv > self.lc.av:
            self.usd = self.quantity * self.lc.dv
        else:
            self.usd = self.quantity * self.lc.av
        pkr = round((self.usd * self.lc.exRate) + self.insurance)
        onePercent = math.ceil(pkr * 0.01)
        self.landingCharges = round(onePercent)
        self.importValuePKR = round(pkr + onePercent)
        self.warehousingCharges = math.ceil(self.importValuePKR * (self.whRate / 100) + 100)
        self.excise = math.ceil(self.importValuePKR * (self.exciseRate / 100) + 10)
        self.stampCharges = 1000
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Vessel: {} LC#: {} B/L#: {} IGM# {}'.format(self.lc.vessel, self.lc.lcNo, self.blNo, self.lc.igm )
    
