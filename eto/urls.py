from django.urls import path

from . import views 
#from .views import AddTerminalView

urlpatterns = [
    path('bl_list/', views.AddTerminalView.as_view(), name='bl_list'),
    #path('bl_list/', views.ListLCView.as_view(), name='bl_list'),


]
