from django.urls import path

from .views import AddClientView, ListClientView, UpdateClientView, DetailClientView

urlpatterns = [
    path('add_client/', AddClientView.as_view(), name='add_client'),
    path('client_list/', ListClientView.as_view(), name='client_list'),
    path('client_detail/<int:pk>', DetailClientView.as_view(), name='client_detail'),
    path('update_client/<int:pk>', UpdateClientView.as_view(), name='update_client'),

]
