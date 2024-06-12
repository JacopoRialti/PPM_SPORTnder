from django import forms
from .models import Event
from django.core.exceptions import ValidationError


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title',
                  'sport',
                  'description',
                  'start_date',
                  'n_participants',
                  'location'
                  ]
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'n_participants': forms.NumberInput(attrs={'min': '1'})
        }


