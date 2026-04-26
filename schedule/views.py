from django.shortcuts import render, redirect
from .models import Meeting
from .forms import MeetingForm

def schedule_home(request):
    return render(request, 'schedule/schedule_home.html')

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