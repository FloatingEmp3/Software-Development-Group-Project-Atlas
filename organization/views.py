from django.shortcuts import render
from .models import Department, Dependency

def organization_home(request):
    departments = Department.objects.all()
    dependencies = Dependency.objects.all()

    return render(request, 'organization/organization.html', {
        'departments': departments,
        'dependencies': dependencies
    })