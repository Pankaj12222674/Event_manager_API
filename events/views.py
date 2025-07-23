from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils.timezone import now

from .models import Event, Booking
from .forms import EventForm

# View: Dashboard
@login_required
def dashboard(request):
    events = Event.objects.all()
    booked = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)
    return render(request, 'dashboard.html', {
        'events': events,
        'booked_ids': list(booked),
    })

# View: Book an event
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Booking.objects.get_or_create(user=request.user, event=event)
    messages.success(request, "You have successfully booked the event.")
    return redirect('dashboard')

# View: Cancel booking
@login_required
def cancel_booking(request, event_id):
    Booking.objects.filter(user=request.user, event_id=event_id).delete()
    messages.info(request, "Your booking has been cancelled.")
    return redirect('dashboard')

# Create event (staff only)
@staff_member_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, "Event created successfully!")
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# Edit event (staff only)
@staff_member_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, "Event updated successfully!")
        return redirect('dashboard')
    return render(request, 'edit_event.html', {'form': form, 'event': event})

# Delete event (staff only)
@staff_member_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.warning(request, "Event deleted successfully.")
        return redirect('dashboard')
    return render(request, 'delete_event.html', {'event': event})

# Booking history (user)
@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    return render(request, 'booking_history.html', {
        'bookings': bookings,
        'current_time': now()
    })
