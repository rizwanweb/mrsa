from django.urls import path

from .views import IBCalculationPDF, NocPDF

urlpatterns = [
    # Reports URLS
    path('ib_calculation/<str:pk>', IBCalculationPDF.as_view(), name='ib_calculation'),
    path('noc/<str:pk>', NocPDF.as_view(), name='noc_sheet'),
]
