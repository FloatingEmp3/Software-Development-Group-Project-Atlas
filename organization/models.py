from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    specialisation = models.TextField()

    def __str__(self):
        return self.name


class Dependency(models.Model):
    team_name = models.CharField(max_length=100)
    depends_on = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team_name} depends on {self.depends_on}"
    
class TeamType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name