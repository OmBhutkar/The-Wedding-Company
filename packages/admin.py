from django.contrib import admin
from .models import Package, PackageService


class PackageServiceInline(admin.TabularInline):
    model = PackageService
    extra = 1


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'guest_capacity_min', 'guest_capacity_max', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    inlines = [PackageServiceInline]
    fieldsets = (
        ('Package Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Capacity', {
            'fields': ('guest_capacity_min', 'guest_capacity_max')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )


@admin.register(PackageService)
class PackageServiceAdmin(admin.ModelAdmin):
    list_display = ['package', 'service_name', 'included']
    list_filter = ['included', 'package']
    search_fields = ['service_name', 'package__name']


