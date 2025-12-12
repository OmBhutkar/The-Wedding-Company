from django import forms
from django.contrib.auth import get_user_model
from .models import Booking, Payment, EventTimeline

User = get_user_model()


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client', 'event_name', 'event_date', 'event_time', 'venue', 'guest_count', 
                  'total_amount', 'advance_paid', 'status', 'notes']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        package = kwargs.pop('package', None)
        super().__init__(*args, **kwargs)
        
        # Set client queryset to all users
        self.fields['client'].queryset = User.objects.all()
        
        # If user is not admin/staff, hide client field and set it automatically
        if user and not (user.is_admin_user() or user.is_staff_user()):
            self.fields['client'].widget = forms.HiddenInput()
            self.fields['client'].initial = user
        
        # Pre-fill form with package details if package is provided
        if package:
            # Set total amount from package price
            if not self.instance.pk:  # Only for new bookings
                self.fields['total_amount'].initial = package.price
                # Set guest count to minimum capacity of package
                self.fields['guest_count'].initial = package.guest_capacity_min
                # Set event name to include package name
                if not self.fields['event_name'].initial:
                    self.fields['event_name'].initial = f"Wedding - {package.name}"
                # Add package info to notes
                if not self.fields['notes'].initial:
                    self.fields['notes'].initial = f"Package: {package.name}\nGuest Capacity: {package.guest_capacity_min}"
                    if package.guest_capacity_max:
                        self.fields['notes'].initial += f" - {package.guest_capacity_max} guests"
        
        for field in self.fields.values():
            if field.widget.__class__.__name__ not in ['CheckboxInput', 'HiddenInput']:
                field.widget.attrs.update({'class': 'form-control'})


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method', 'payment_date', 'transaction_id', 'notes']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class EventTimelineForm(forms.ModelForm):
    class Meta:
        model = EventTimeline
        fields = ['title', 'description', 'scheduled_time', 'completed']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.widget.__class__.__name__ != 'CheckboxInput':
                field.widget.attrs.update({'class': 'form-control'})

