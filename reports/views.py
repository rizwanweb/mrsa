from django.shortcuts import render
from .utils import render_to_pdf
import math
from num2words import num2words
from collections import Counter

from lc.models import LC
from bl.models import BL
from item.models import ItemDutyStructure

from django.views.generic import View
# Create your views here.


class IBCalculationPDF(View):
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        lc = LC.objects.get(id=pk)
        bls = lc.bl_set.all()

        #get Duplicates
        dups = []
        for bl in bls:
            dups.append(bl.quantity)
        dups = dict(Counter(dups))
        
        # Get PSQC
        totalBL = BL.objects.filter(
            lc__item=lc.item, lc__igm=lc.igm, lc__client=lc.client)
        sumBL = 0
        for bl in totalBL:
            sumBL += bl.importValuePKR
        sumBL = round(sumBL)
        psqc = round((sumBL * (0.05/100))+11000)

        context = {
            'dups': dups,
            'psqc': psqc,
            'lc': lc,
            'bls': bls,

        }
        pdf = render_to_pdf('reports/ib_warehousing.html', context)
        return pdf


class NocPDF(View):
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        lc = LC.objects.get(id=pk)
        bls = lc.bl_set.all()

        dutyItem = ItemDutyStructure.objects.get(item=lc.item)
        insuranceUSD = 0

        for bl in bls:
            insuranceUSD = round(bl.insurance / lc.exRate)
            if dutyItem.cdType == 'F':
                cd = dutyItem.cdRate * bl.quantity
            else:
                cd = (dutyItem.cdRate / 100) * bl.importValuePKR

            if dutyItem.rdType == 'F':
                rd = dutyItem.rdRate * bl.quantity
            else:
                rd = "i dont know the calculation"

            acd = math.ceil((dutyItem.acdRate / 100) * bl.importValuePKR)
            st = math.ceil((bl.importValuePKR + cd + acd + rd)
                           * (dutyItem.stRate / 100) + 100)
            it = math.ceil((bl.importValuePKR + cd + rd + acd + st)
                           * (dutyItem.itRate / 100)+2)

        total = cd + rd + acd + st + it

        context = {
            'dutyItem': dutyItem,
            'total': total,
            'it': it,
            'st': st,
            'cd': cd,
            'rd': rd,
            'acd': acd,
            'ins': insuranceUSD,
            'lc': lc,
            'bls': bls,
        }
        pdf = render_to_pdf('reports/noc.html', context)
        return pdf


class AllowPDF(View):
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        lc = LC.objects.get(id=pk)
        bls = lc.bl_set.all()
        context = {
            'lc': lc,
            'bls': bls,
        }
        pdf = render_to_pdf('reports/allow.html', context)
        return pdf

class WharfagePDF(View):
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        lc = LC.objects.get(id=pk)
        bls = lc.bl_set.all()

        wharfage = math.ceil(lc.totalQuantity) * 31
        sst = wharfage * (lc.fed/100)
        inwords = num2words(lc.pqaCharges)
        print(inwords)

        blno = []
        for bl in bls:
            blno.append(bl.blNo[-3:])
        blno.pop(0)
        for n in blno:
            print(n)
        context = {
            'blno': blno,
            'inwords': inwords,
            'wharfage': wharfage,
            'sst': sst,
            'lc': lc,
            'bls': bls,
        }
        pdf = render_to_pdf('reports/wharfage.html', context)
        return pdf


class BondPDF(View): # Indemnity Bond PDF
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        bl = BL.objects.get(id=pk)
        context = {
            'bl': bl,
        }
        pdf = render_to_pdf('reports/bond.html', context)
        return pdf

class Bond2PDF(View): #Second Page of Indemnity Bond PDF
    #login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        bl = BL.objects.get(id=pk)
        context = {
            'bl': bl,
        }
        pdf = render_to_pdf('reports/bond2.html', context)
        return pdf