from django.contrib import admin
from django.urls import path, include   
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('teams/', include('teams.urls')), 
    path('reports/', include('reports.urls')),
    path('schedule/', include('schedule.urls')),
    path('organization/', include('organization.urls')),
]