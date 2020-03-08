from django.urls import path
from . import views


urlpatterns = [
    # Ex: /targets/5/
    path('', views.index, name='index'),
    path('<int:target_id>/', views.detail, name='detail')

]
