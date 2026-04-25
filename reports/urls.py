from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_dashboard, name='reports'),
    path('pdf/', views.generate_pdf, name='report_pdf'),
    path('excel/', views.generate_excel, name='report_excel'),
]