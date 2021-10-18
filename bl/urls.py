from django.urls import path

from . import views

urlpatterns = [
    path('psqc/<int:pk>', views.psqc, name='psqc'),

    path('add_bl/', views.createBL, name='add_bl'),
]
