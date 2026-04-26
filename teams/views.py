from django.shortcuts import render
from django.db.models import Q
from .models import Team

#Eduardo Lamasanu w2078922

def team_list(request):
    query = request.GET.get('q')

    if query:
        teams = Team.objects.filter(
            Q(team_name__icontains=query) |
            Q(team_leader__icontains=query) |
            Q(department__icontains=query) |
            Q(skills__icontains=query)
        )
    else:
        teams = Team.objects.all()

    return render(request, 'teams/team_list.html', {'teams': teams, 'query': query})