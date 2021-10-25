from django.urls import path

from . import views 
from .views import AddTerminalView

urlpatterns = [
    path('bl_list/', views.AddTerminalView.as_view(), name='bl_list'),
    path('allow_list/', views.BLListView.as_view(), name='allow_list'),
    path('add_terminal/<int:pk>', views.UpdateTerminalView.as_view(), name='add_terminal'),
    #path('bl_list/', views.ListLCView.as_view(), name='bl_list'),


]
