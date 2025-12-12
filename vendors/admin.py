from django.contrib import admin
from .models import VendorCategory, Vendor, VendorAssignment


@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'contact_person', 'phone', 'base_price', 'is_active', 'rating']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'contact_person', 'email', 'phone']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'contact_person', 'email', 'phone', 'address')
        }),
        ('Service Details', {
            'fields': ('service_description', 'base_price', 'rating')
        }),
        ('Status', {
            'fields': ('is_active', 'notes')
        }),
    )


@admin.register(VendorAssignment)
class VendorAssignmentAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'booking', 'service_date', 'service_time', 'agreed_price']
    list_filter = ['service_date', 'created_at']
    search_fields = ['vendor__name', 'booking__event_name']


