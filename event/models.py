from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    n_participants = models.IntegerField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')  # User who created the event
    registered_users = models.ManyToManyField(User, related_name='registered_events')  # Users who registered for the event

    def __str__(self):
        return self.title


