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
            event.registered_users.add(request.user)
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def show_events(request):
    created_events = Event.objects.filter(organizer=request.user).order_by('start_date')
    registered_events = request.user.registered_events.exclude(organizer=request.user).order_by('start_date')
    return render(request, 'show_events.html', {'created_events': created_events, 'registered_events': registered_events})


@login_required
def show_all_events(request):
    all_events = Event.objects.annotate(num_registered_users=Count('registered_users')).filter(num_registered_users__lt=F('n_participants')).order_by('start_date')
    return render(request, 'show_all_events.html', {'all_events': all_events, 'user': request.user})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.remaining_slots = event.n_participants - event.registered_users.count()
    return render(request, 'event_detail.html', {'event': event})
