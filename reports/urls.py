from django.urls import path

from .views import IBCalculationPDF, NocPDF, AllowPDF, BondPDF

urlpatterns = [
    # Reports URLS
    path('ib_calculation/<str:pk>', IBCalculationPDF.as_view(), name='ib_calculation'),
    path('noc/<str:pk>', NocPDF.as_view(), name='noc_sheet'),
    path('allow/<str:pk>', AllowPDF.as_view(), name='allow'),
    path('bond/<str:pk>', BondPDF.as_view(), name='bond'),
]
