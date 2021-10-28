from django.urls import path

from . import views 
from .views import AddTerminalView, AddPayorderView

urlpatterns = [
    path('bl_list/', views.AddTerminalView.as_view(), name='bl_list'),
    path('allow_list/', views.BLListView.as_view(), name='allow_list'),
    path('wharfage_list/', views.AddPayorderView.as_view(), name='wharfage_list'),
    path('add_wharfage/<int:pk>', views.UpdatePQAView.as_view(), name='add_wharfage'),
    path('add_terminal/<int:pk>', views.UpdateTerminalView.as_view(), name='add_terminal'),
    path('bond_list/', views.BondListView.as_view(), name='bond_list'),


]
