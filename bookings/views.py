from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from django.utils import timezone
from django import forms
from .models import Booking, Payment, EventTimeline
from .forms import BookingForm, PaymentForm, EventTimelineForm


@login_required
def dashboard(request):
    """Main dashboard view"""
    user = request.user
    
    # Get bookings based on user role
    if user.is_admin_user() or user.is_staff_user():
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(client=user)
    
    # Statistics
    total_bookings = bookings.count()
    pending_bookings = bookings.filter(status='pending').count()
    confirmed_bookings = bookings.filter(status='confirmed').count()
    upcoming_bookings = bookings.filter(event_date__gte=timezone.now().date()).count()
    
    # Recent bookings
    recent_bookings = bookings[:5]
    
    # Upcoming events
    upcoming_events = bookings.filter(
        event_date__gte=timezone.now().date(),
        status__in=['confirmed', 'in_progress']
    ).order_by('event_date')[:5]
    
    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'upcoming_bookings': upcoming_bookings,
        'recent_bookings': recent_bookings,
        'upcoming_events': upcoming_events,
    }
    
    return render(request, 'bookings/dashboard.html', context)


@login_required
def booking_list(request):
    """List all bookings"""
    user = request.user
    
    if user.is_admin_user() or user.is_staff_user():
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(client=user)
    
    # Filtering
    status_filter = request.GET.get('status')
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    search_query = request.GET.get('search')
    if search_query:
        bookings = bookings.filter(
            Q(event_name__icontains=search_query) |
            Q(venue__icontains=search_query) |
            Q(client__username__icontains=search_query)
        )
    
    context = {
        'bookings': bookings,
        'status_filter': status_filter,
        'search_query': search_query,
    }
    
    return render(request, 'bookings/booking_list.html', context)


@login_required
def booking_detail(request, pk):
    """Booking detail view"""
    user = request.user
    
    if user.is_admin_user() or user.is_staff_user():
        booking = get_object_or_404(Booking, pk=pk)
    else:
        booking = get_object_or_404(Booking, pk=pk, client=user)
    
    payments = booking.payments.all()
    timeline_items = booking.timeline_items.all()
    
    context = {
        'booking': booking,
        'payments': payments,
        'timeline_items': timeline_items,
    }
    
    return render(request, 'bookings/booking_detail.html', context)


@login_required
def booking_create(request):
    """Create new booking"""
    package_id = request.GET.get('package_id')
    package = None
    
    # Get package details if package_id is provided
    if package_id:
        try:
            from packages.models import Package
            package = Package.objects.get(pk=package_id, is_active=True)
        except Package.DoesNotExist:
            messages.warning(request, 'Selected package not found or inactive.')
    
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user, package=package)
        if form.is_valid():
            booking = form.save(commit=False)
            # If user is not admin/staff, ensure client is set to current user
            if not request.user.is_admin_user() and not request.user.is_staff_user():
                booking.client = request.user
            # Ensure client is set (for admin/staff, it should come from form)
            if not booking.client:
                booking.client = request.user
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        form = BookingForm(user=request.user, package=package)
    
    return render(request, 'bookings/booking_form.html', {
        'form': form, 
        'title': 'Create Booking',
        'package': package
    })


@login_required
def booking_update(request, pk):
    """Update booking"""
    user = request.user
    
    if user.is_admin_user() or user.is_staff_user():
        booking = get_object_or_404(Booking, pk=pk)
    else:
        booking = get_object_or_404(Booking, pk=pk, client=user)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            # If user is not admin/staff, ensure client cannot be changed
            if not request.user.is_admin_user() and not request.user.is_staff_user():
                booking.client = request.user
            booking.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking, user=request.user)
    
    return render(request, 'bookings/booking_form.html', {'form': form, 'title': 'Update Booking', 'booking': booking})


@login_required
def payment_create(request, booking_pk):
    """Add payment for a booking"""
    booking = get_object_or_404(Booking, pk=booking_pk)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            
            # Update booking advance_paid
            total_payments = booking.payments.aggregate(Sum('amount'))['amount__sum'] or 0
            booking.advance_paid = total_payments
            booking.save()
            
            messages.success(request, 'Payment recorded successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        form = PaymentForm()
    
    return render(request, 'bookings/payment_form.html', {'form': form, 'booking': booking})


@login_required
def timeline_create(request, booking_pk):
    """Add timeline item for a booking"""
    booking = get_object_or_404(Booking, pk=booking_pk)
    
    if request.method == 'POST':
        form = EventTimelineForm(request.POST)
        if form.is_valid():
            timeline = form.save(commit=False)
            timeline.booking = booking
            timeline.save()
            messages.success(request, 'Timeline item added successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        form = EventTimelineForm()
    
    return render(request, 'bookings/timeline_form.html', {'form': form, 'booking': booking})

