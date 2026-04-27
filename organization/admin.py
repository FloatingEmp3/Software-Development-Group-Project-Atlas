from django.contrib import admin
from .models import Department, Dependency, TeamType

admin.site.register(Department)
admin.site.register(Dependency)
admin.site.register(TeamType)