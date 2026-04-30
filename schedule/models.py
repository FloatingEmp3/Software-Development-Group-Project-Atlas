#Naglis Bumbulis (20869300)
from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    PLATFORM_CHOICES = [
        ('zoom', 'Zoom'),
        ('teams', 'Microsoft Teams'),
        ('in_person', 'In Person'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title