from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('client', 'Client'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    def is_admin_user(self):
        return self.role == 'admin' or self.is_superuser
    
    def is_staff_user(self):
        return self.role == 'staff' or self.is_admin_user()


class ClientProfile(models.Model):
    """Extended profile for clients"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=15, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - Client Profile"


