from django.db import models

class Team(models.Model):
    department = models.CharField(max_length=100)
    team_leader = models.CharField(max_length=100)
    department_head = models.CharField(max_length=100, blank=True)
    team_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100, blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    focus_areas = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    upstream_dependencies = models.TextField(blank=True)
    downstream_dependencies = models.TextField(blank=True)
    slack_channels = models.TextField(blank=True)
    team_wiki = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.team_name