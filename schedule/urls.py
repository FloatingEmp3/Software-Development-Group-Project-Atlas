#Naglis Bumbulis (20869300)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='schedule_home'),
    path('create/', views.create_meeting, name='create_meeting'),
    path('weekly/', views.weekly_view, name='weekly_view'),
    path('monthly/', views.monthly_view, name='monthly_view'),
    path('delete/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),
]