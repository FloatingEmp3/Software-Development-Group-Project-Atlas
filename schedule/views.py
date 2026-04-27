from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Meeting
from .forms import MeetingForm
from datetime import date, timedelta

def schedule_home(request):
    today = date.today()
    meetings = Meeting.objects.filter(date__gte=today).order_by('date', 'time')
    return render(request, 'schedule/schedule_home.html', {'meetings': meetings, 'today': today})

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.created_by = request.user
            meeting.save()
            return redirect('schedule_home')
    else:
        form = MeetingForm()
    return render(request, 'schedule/meeting_form.html', {'form': form})

def weekly_view(request):
    today = date.today()
    week_end = today + timedelta(days=7)
    meetings = Meeting.objects.filter(date__gte=today, date__lte=week_end).order_by('date', 'time')
    return render(request, 'schedule/weekly_view.html', {'meetings': meetings, 'today': today, 'week_end': week_end})

def monthly_view(request):
    today = date.today()
    month_end = today + timedelta(days=30)
    meetings = Meeting.objects.filter(date__gte=today, date__lte=month_end).order_by('date', 'time')
    return render(request, 'schedule/monthly_view.html', {'meetings': meetings, 'today': today, 'month_end': month_end})