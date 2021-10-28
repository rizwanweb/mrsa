from django.urls import path

from .views import IBCalculationPDF, NocPDF, AllowPDF, BondPDF, Bond2PDF, WharfagePDF

urlpatterns = [
    # Reports URLS
    path('ib_calculation/<str:pk>', IBCalculationPDF.as_view(), name='ib_calculation'),
    path('noc/<str:pk>', NocPDF.as_view(), name='noc_sheet'),
    path('allow/<str:pk>', AllowPDF.as_view(), name='allow'),
    path('wharfage/<str:pk>', WharfagePDF.as_view(), name='wharfage'),
    path('bond/<str:pk>', BondPDF.as_view(), name='bond'),
    path('bond2/<str:pk>', Bond2PDF.as_view(), name='bond2'),
]
