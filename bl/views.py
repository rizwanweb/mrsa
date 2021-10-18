from django.shortcuts import render, redirect

from django.forms.models import inlineformset_factory
from django.db.models import Sum

from lc.models import LC
from .models import BL
# Create your views here.


def createBL(request):
    lc = LC.objects.latest('id')
    totalBL = lc.totalBL
    blFormSet = inlineformset_factory(LC, BL, fields=(
        'blNo', 'blDate', 'quantity', 'index', 'whRate', 'exciseRate'), extra=totalBL)
    formset = blFormSet()

    if request.method == "POST":
        formset = blFormSet(request.POST)
        if formset.is_valid():
            instance = formset.save(commit=False)
            for i in instance:
                i.lc = lc
                i.save()
            return redirect('index')
        else:
            print(formset.errors)

    context = {
        'lc': lc,
        'totalBL': totalBL,
        'formset': blFormSet
    }
    return render(request, 'bl/add_bl.html', context)


def psqc(request, pk):
    lc = LC.objects.get(id=pk)

    #sum = lc.get_sum_of_bl()

    totalBL = BL.objects.filter(
        lc__item=lc.item, lc__igm=lc.igm, lc__client=lc.client)

    sumBL = 0

    for bl in totalBL:
        sumBL += bl.importValuePKR
        print(sumBL)
    print(sumBL)

    sumBL = round(sumBL)

    psqc = round((sumBL * 0.005)+11000)
    context = {
        'psqc': psqc,
        'sumBL': sumBL,
        'lc': lc,
        'totalBL': totalBL,
        # 'sum': sum
    }
    return render(request, 'bl/psqc.html', context)
