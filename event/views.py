from django.utils import timezone

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.shortcuts import get_object_or_404


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            event.registered_users.add(request.user)
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def show_events(request):
    now = timezone.now()
    created_events = Event.objects.filter(organizer=request.user, start_date__gt=now).order_by('start_date')
    registered_events = request.user.registered_events.exclude(organizer=request.user).exclude(start_date__lt=now).order_by('start_date')
    last_events = request.user.registered_events.exclude(start_date__gt=now).order_by('-start_date')
    return render(request, 'show_events.html', {'created_events': created_events,
                                                'registered_events': registered_events,
                                                'last_events': last_events})


@login_required
def show_all_events(request):
    now = timezone.now()
    all_events = Event.objects.annotate(num_registered_users=Count('registered_users')).filter(num_registered_users__lt=F('n_participants')).exclude(start_date__lt=now).order_by('start_date')
    return render(request, 'show_all_events.html', {'all_events': all_events, 'user': request.user})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.remaining_slots = event.n_participants - event.registered_users.count()
    context = {
        'event': event,
        'registered_users': event.registered_users.all()
    }
    return render(request, 'event_detail.html', context)


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    context = {
        'form': form,
        'users_registered': event.registered_users.all(),
        'event': event
    }
    return render(request, 'edit_event.html', context)


@login_required
def remove_user_from_event(request, event_id, user_id):
    event = get_object_or_404(Event, id=event_id)
    user = get_object_or_404(User, id=user_id)
    if request.user == event.organizer:
        event.registered_users.remove(user)
    return redirect('event_detail', event_id=event.id)


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.organizer:
        event.delete()
    return redirect('home')


