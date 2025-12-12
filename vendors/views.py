from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django import forms
from django.utils import timezone
from .models import Vendor, VendorCategory, VendorAssignment
from .forms import VendorForm, VendorAssignmentForm
from bookings.models import Booking


@login_required
def vendor_list(request):
    """List all vendors"""
    vendors = Vendor.objects.filter(is_active=True)
    
    category_filter = request.GET.get('category')
    if category_filter:
        vendors = vendors.filter(category_id=category_filter)
    
    search_query = request.GET.get('search')
    if search_query:
        vendors = vendors.filter(
            Q(name__icontains=search_query) |
            Q(contact_person__icontains=search_query) |
            Q(service_description__icontains=search_query)
        )
    
    categories = VendorCategory.objects.all()
    
    context = {
        'vendors': vendors,
        'categories': categories,
        'category_filter': category_filter,
        'search_query': search_query,
    }
    
    return render(request, 'vendors/vendor_list.html', context)


@login_required
def vendor_detail(request, pk):
    """Vendor detail view"""
    vendor = get_object_or_404(Vendor, pk=pk)
    assignments = vendor.assignments.all()[:10]  # Recent assignments
    
    context = {
        'vendor': vendor,
        'assignments': assignments,
    }
    
    return render(request, 'vendors/vendor_detail.html', context)


@login_required
def vendor_create(request):
    """Create new vendor"""
    if not request.user.is_admin_user() and not request.user.is_staff_user():
        messages.error(request, 'You do not have permission to create vendors.')
        return redirect('vendors:vendor_list')
    
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor created successfully!')
            return redirect('vendors:vendor_list')
    else:
        form = VendorForm()
    
    return render(request, 'vendors/vendor_form.html', {'form': form, 'title': 'Create Vendor'})


@login_required
def vendor_update(request, pk):
    """Update vendor"""
    if not request.user.is_admin_user() and not request.user.is_staff_user():
        messages.error(request, 'You do not have permission to update vendors.')
        return redirect('vendors:vendor_list')
    
    vendor = get_object_or_404(Vendor, pk=pk)
    
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor updated successfully!')
            return redirect('vendors:vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    
    return render(request, 'vendors/vendor_form.html', {'form': form, 'title': 'Update Vendor', 'vendor': vendor})


@login_required
def vendor_assign(request, booking_pk):
    """Assign vendor to booking"""
    booking = get_object_or_404(Booking, pk=booking_pk)
    
    if request.method == 'POST':
        form = VendorAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.booking = booking
            assignment.save()
            messages.success(request, 'Vendor assigned successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        form = VendorAssignmentForm()
    
    return render(request, 'vendors/vendor_assign_form.html', {'form': form, 'booking': booking})


@login_required
def vendor_assign_from_detail(request, vendor_pk):
    """Assign vendor from vendor detail page - show booking selection"""
    vendor = get_object_or_404(Vendor, pk=vendor_pk)
    
    # Get user's bookings
    user = request.user
    if user.is_admin_user() or user.is_staff_user():
        bookings = Booking.objects.all().order_by('-event_date')
    else:
        bookings = Booking.objects.filter(client=user).order_by('-event_date')
    
    # Filter to show only upcoming or recent bookings
    from django.utils import timezone
    bookings = bookings.filter(event_date__gte=timezone.now().date() - timezone.timedelta(days=30))
    
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            booking = get_object_or_404(Booking, pk=booking_id)
            # Redirect to assignment form with vendor pre-selected
            return redirect('vendors:vendor_assign_to_booking', vendor_pk=vendor.pk, booking_pk=booking.pk)
        else:
            messages.error(request, 'Please select a booking.')
    
    context = {
        'vendor': vendor,
        'bookings': bookings,
    }
    
    return render(request, 'vendors/vendor_assign_select_booking.html', context)


@login_required
def vendor_assign_to_booking(request, vendor_pk, booking_pk):
    """Assign specific vendor to specific booking"""
    vendor = get_object_or_404(Vendor, pk=vendor_pk)
    booking = get_object_or_404(Booking, pk=booking_pk)
    
    # Check if user has access to this booking
    user = request.user
    if not user.is_admin_user() and not user.is_staff_user():
        if booking.client != user:
            messages.error(request, 'You do not have permission to assign vendors to this booking.')
            return redirect('vendors:vendor_detail', pk=vendor.pk)
    
    if request.method == 'POST':
        form = VendorAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.vendor = vendor
            assignment.booking = booking
            assignment.save()
            messages.success(request, f'{vendor.name} assigned to {booking.event_name} successfully!')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        # Pre-fill form with vendor and booking details
        form = VendorAssignmentForm(initial={
            'vendor': vendor,
            'service_date': booking.event_date,
            'service_time': booking.event_time,
            'agreed_price': vendor.base_price,
        })
        form.fields['vendor'].widget = forms.HiddenInput()
    
    context = {
        'form': form,
        'vendor': vendor,
        'booking': booking,
    }
    
    return render(request, 'vendors/vendor_assign_form.html', context)

