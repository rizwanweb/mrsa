from django.urls import path

from lc.views import AddLCView, ListLCView, UpdateLCView

urlpatterns = [
    path('create_lc/', AddLCView.as_view(), name='add_lc'),
    path('lc_list/', ListLCView.as_view(), name='lc_list'),
    path('update_lc/<int:pk>', UpdateLCView.as_view(), name='update_lc')
]
