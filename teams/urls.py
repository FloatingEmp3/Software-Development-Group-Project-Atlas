from django.urls import path
from . import views

#Eduardo Lamasanu w2078922

urlpatterns = [
    path('', views.team_list, name='team_list'),
]