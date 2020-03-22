from django.urls import path
from . import views


urlpatterns = [
    path('', views.TargetList.as_view(), name='target_list'),
    path('view/<int:pk>', views.TargetView.as_view(), name='target_view'),
    path('new', views.TargetCreate.as_view(), name='target_new'),
    path('view/<int:pk>', views.TargetView.as_view(), name='target_view'),
    path('edit/<int:pk>', views.TargetUpdate.as_view(), name='target_edit'),
    path('delete/<int:pk>', views.TargetDelete.as_view(), name='target_delete'),
]