from django.urls import path
from . import views

urlpatterns = [
    path('', views.organization_home, name='organization_home'),
]