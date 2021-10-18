from django.db import models

# Create your models here.
#from bl.models import BL

DUTY_TYPE = (
    ('%', '%'),
    ('F', 'F'),
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    pct = models.CharField(max_length=20)

    # Exemption

    def __str__(self):
        return self.name


class ItemDutyStructure(models.Model):
    #bl = models.ForeignKey(BL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cdRate = models.FloatField()
    cdType = models.CharField(max_length=5, choices=DUTY_TYPE, default='F')
    rdRate = models.FloatField()
    rdType = models.CharField(max_length=5, choices=DUTY_TYPE, default='F')
    acdRate = models.FloatField()
    acdType = models.CharField(max_length=5, choices=DUTY_TYPE, default='%')
    stRate = models.FloatField()
    itRate = models.FloatField()
    fed = models.FloatField()
    fedType = models.CharField(max_length=5, choices=DUTY_TYPE, default='F')

    # def get_cd(self):
    #     cd = self.cdRate * BL.quantity
    #     return cd

    def __str__(self):
        return self.item.name
