from django.shortcuts import render

def schedule_home(request):
    return render(request, 'schedule/schedule_home.html')
