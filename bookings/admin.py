from django.contrib import admin
from .models import Booking, Payment, EventTimeline


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'client', 'event_date', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'event_date', 'created_at']
    search_fields = ['event_name', 'client__username', 'venue']
    readonly_fields = ['remaining_amount', 'created_at', 'updated_at']
    fieldsets = (
        ('Event Details', {
            'fields': ('client', 'event_name', 'event_date', 'event_time', 'venue', 'guest_count')
        }),
        ('Financial Details', {
            'fields': ('total_amount', 'advance_paid', 'remaining_amount')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'payment_method', 'payment_date', 'created_at']
    list_filter = ['payment_method', 'payment_date']
    search_fields = ['booking__event_name', 'transaction_id']


@admin.register(EventTimeline)
class EventTimelineAdmin(admin.ModelAdmin):
    list_display = ['title', 'booking', 'scheduled_time', 'completed']
    list_filter = ['completed', 'scheduled_time']
    search_fields = ['title', 'booking__event_name']


