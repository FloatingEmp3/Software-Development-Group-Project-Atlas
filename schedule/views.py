from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Meeting
from .forms import MeetingForm
from datetime import date

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