from django.urls import path
from . import views

urlpatterns = [
    path('', views.zapros_list, name='zapros_list'),
]
