from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from decimal import Decimal

User = get_user_model()


class Booking(models.Model):
    """Wedding booking model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=200)
    guest_count = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    advance_paid = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-event_date', '-created_at']
    
    def __str__(self):
        return f"{self.event_name} - {self.client.username} - {self.event_date}"
    
    def save(self, *args, **kwargs):
        self.remaining_amount = self.total_amount - self.advance_paid
        super().save(*args, **kwargs)


class Payment(models.Model):
    """Payment tracking model"""
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI'),
        ('cheque', 'Cheque'),
    ]
    
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField()
    transaction_id = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment of {self.amount} for {self.booking.event_name}"


class EventTimeline(models.Model):
    """Event timeline/checklist model"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='timeline_items')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    scheduled_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['scheduled_time']
    
    def __str__(self):
        return f"{self.title} - {self.booking.event_name}"


