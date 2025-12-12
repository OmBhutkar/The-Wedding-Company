# Generated manually to add 2 more wedding packages

from django.db import migrations


def create_additional_packages(apps, schema_editor):
    """Create 2 additional wedding packages with services"""
    Package = apps.get_model('packages', 'Package')
    PackageService = apps.get_model('packages', 'PackageService')
    
    packages_data = [
        {
            'name': 'Starter Wedding Package',
            'description': 'Perfect for budget-conscious couples who want a beautiful wedding without breaking the bank. Essential services at an affordable price.',
            'price': 2000.00,
            'guest_capacity_min': 30,
            'guest_capacity_max': 75,
            'features': '''Basic venue setup
Photography (3 hours)
Simple catering
Music system
Wedding cake
Basic flowers
Event assistance''',
            'services': [
                {'service_name': 'Basic Setup', 'description': 'Simple venue decoration and setup', 'included': True},
                {'service_name': 'Photography', 'description': '3 hours of photography coverage', 'included': True},
                {'service_name': 'Simple Catering', 'description': 'Basic meal service for up to 75 guests', 'included': True},
                {'service_name': 'Music System', 'description': 'Basic sound system and music playlist', 'included': True},
                {'service_name': 'Wedding Cake', 'description': 'Simple 1-tier wedding cake', 'included': True},
                {'service_name': 'Basic Flowers', 'description': 'Simple floral arrangements', 'included': True},
                {'service_name': 'Event Assistance', 'description': 'Basic day-of assistance', 'included': True},
            ]
        },
        {
            'name': 'Deluxe Wedding Package',
            'description': 'An exclusive package combining luxury and elegance. Perfect for couples who want premium services with personalized attention to every detail.',
            'price': 22000.00,
            'guest_capacity_min': 180,
            'guest_capacity_max': 400,
            'features': '''Exclusive venue decoration
Elite photography (full day) + Cinematic videography
Gourmet catering with live stations
Premium entertainment ensemble
Designer multi-tier cake
Luxury floral design
Dedicated wedding planner
Luxury bridal and groom suites
Premium transportation
Elite lighting and production
Professional photo booth
Premium wedding favors
Welcome reception
Day-after brunch
Honeymoon consultation
Customization options''',
            'services': [
                {'service_name': 'Exclusive Decoration', 'description': 'Designer-level exclusive decoration with custom themes', 'included': True},
                {'service_name': 'Elite Photography & Videography', 'description': 'Full day coverage with cinematic film production', 'included': True},
                {'service_name': 'Gourmet Catering', 'description': 'Multi-course gourmet meal with live cooking stations', 'included': True},
                {'service_name': 'Premium Entertainment', 'description': 'Elite live band, DJ, and special performances', 'included': True},
                {'service_name': 'Designer Multi-Tier Cake', 'description': 'Custom designer cake with multiple flavors and designs', 'included': True},
                {'service_name': 'Luxury Floral Design', 'description': 'Premium designer floral arrangements and installations', 'included': True},
                {'service_name': 'Dedicated Planner', 'description': 'Personal wedding planner throughout the process', 'included': True},
                {'service_name': 'Luxury Suites', 'description': 'Premium suite preparation for entire bridal party', 'included': True},
                {'service_name': 'Premium Transportation', 'description': 'Luxury vehicle service for bridal party and guests', 'included': True},
                {'service_name': 'Elite Production', 'description': 'Professional lighting, sound, and production design', 'included': True},
                {'service_name': 'Professional Photo Booth', 'description': 'Premium photo booth with instant prints and props', 'included': True},
                {'service_name': 'Premium Favors', 'description': 'Luxury wedding favors and gifts for all guests', 'included': True},
                {'service_name': 'Welcome Reception', 'description': 'Welcome reception and rehearsal dinner coordination', 'included': True},
                {'service_name': 'Day-After Brunch', 'description': 'Post-wedding brunch for all guests', 'included': True},
                {'service_name': 'Honeymoon Consultation', 'description': 'Personalized honeymoon planning assistance', 'included': True},
                {'service_name': 'Customization Options', 'description': 'Custom package modifications and add-ons', 'included': True},
            ]
        },
    ]
    
    for package_data in packages_data:
        services = package_data.pop('services')
        package, created = Package.objects.get_or_create(
            name=package_data['name'],
            defaults=package_data
        )
        
        if created:
            # Add services to the package
            for service_data in services:
                PackageService.objects.create(
                    package=package,
                    **service_data
                )


def remove_additional_packages(apps, schema_editor):
    """Remove additional packages"""
    Package = apps.get_model('packages', 'Package')
    
    package_names = [
        'Starter Wedding Package',
        'Deluxe Wedding Package'
    ]
    
    Package.objects.filter(name__in=package_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_add_default_packages'),
    ]

    operations = [
        migrations.RunPython(create_additional_packages, remove_additional_packages),
    ]


