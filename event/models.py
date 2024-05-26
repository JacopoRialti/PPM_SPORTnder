from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)  # Optional end date
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')  # User who created the event
    category = models.CharField(max_length=100, blank=True)  # Optional category
    image = models.ImageField(upload_to='events/', blank=True)  # Optional image for the event
    speaker = models.CharField(max_length=255, blank=True)  # Optional speaker name

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)  # Timestamp of registration

    class Meta:
        unique_together = ('user', 'event')  # Enforce unique registration per user per event

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"

