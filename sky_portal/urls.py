from django.contrib import admin
from django.urls import path, include   
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from sky_portal import views

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('teams/', include('teams.urls')), 
    path('reports/', include('reports.urls')),
    path('schedule/', include('schedule.urls')),
    path('organization/', include('organization.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
]