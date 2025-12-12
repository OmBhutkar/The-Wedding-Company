from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Package(models.Model):
    """Wedding package model"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    guest_capacity_min = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    guest_capacity_max = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    features = models.TextField(help_text="List of features separated by commas or new lines")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['price']
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    def get_features_list(self):
        """Return features as a list"""
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class PackageService(models.Model):
    """Services included in a package"""
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    included = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['service_name']
    
    def __str__(self):
        return f"{self.package.name} - {self.service_name}"


