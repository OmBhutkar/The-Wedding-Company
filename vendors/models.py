from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class VendorCategory(models.Model):
    """Vendor category model"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Vendor Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Vendor(models.Model):
    """Vendor model"""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(VendorCategory, on_delete=models.SET_NULL, null=True, related_name='vendors')
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    service_description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.00'), 
                                 validators=[MinValueValidator(Decimal('0.00'))])
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.category}"


class VendorAssignment(models.Model):
    """Vendor assignment to bookings"""
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE, related_name='vendor_assignments')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='assignments')
    service_date = models.DateField()
    service_time = models.TimeField()
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['service_date', 'service_time']
        unique_together = ['booking', 'vendor', 'service_date']
    
    def __str__(self):
        return f"{self.vendor.name} - {self.booking.event_name}"

