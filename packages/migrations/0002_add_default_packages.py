# Generated manually to add default wedding packages

from django.db import migrations


def create_default_packages(apps, schema_editor):
    """Create default wedding packages with services"""
    Package = apps.get_model('packages', 'Package')
    PackageService = apps.get_model('packages', 'PackageService')
    
    packages_data = [
        {
            'name': 'Basic Wedding Package',
            'description': 'Perfect for intimate weddings with essential services. Ideal for couples looking for a simple yet elegant celebration.',
            'price': 3500.00,
            'guest_capacity_min': 50,
            'guest_capacity_max': 100,
            'features': '''Venue decoration
Basic photography (4 hours)
Catering for up to 100 guests
DJ and sound system
Wedding cake
Basic floral arrangements
Event coordination
Setup and cleanup''',
            'services': [
                {'service_name': 'Venue Decoration', 'description': 'Basic decoration setup for ceremony and reception', 'included': True},
                {'service_name': 'Photography', 'description': '4 hours of photography coverage', 'included': True},
                {'service_name': 'Catering', 'description': 'Buffet style catering for up to 100 guests', 'included': True},
                {'service_name': 'Music & Sound', 'description': 'DJ services and sound system', 'included': True},
                {'service_name': 'Wedding Cake', 'description': '2-tier wedding cake', 'included': True},
                {'service_name': 'Floral Arrangements', 'description': 'Basic centerpieces and bridal bouquet', 'included': True},
                {'service_name': 'Event Coordination', 'description': 'Day-of coordination services', 'included': True},
            ]
        },
        {
            'name': 'Standard Wedding Package',
            'description': 'A comprehensive package with all essential services plus some premium additions. Great value for medium-sized weddings.',
            'price': 7500.00,
            'guest_capacity_min': 100,
            'guest_capacity_max': 200,
            'features': '''Premium venue decoration
Professional photography (8 hours) + Videography
Full catering service with multiple options
Live band or premium DJ
Custom wedding cake
Premium floral arrangements
Full event planning and coordination
Bridal suite preparation
Transportation service
Lighting and special effects''',
            'services': [
                {'service_name': 'Premium Decoration', 'description': 'Full venue decoration with custom themes', 'included': True},
                {'service_name': 'Photography & Videography', 'description': '8 hours coverage with professional videographer', 'included': True},
                {'service_name': 'Full Catering', 'description': 'Multi-course meal with multiple options', 'included': True},
                {'service_name': 'Entertainment', 'description': 'Live band or premium DJ with MC', 'included': True},
                {'service_name': 'Custom Wedding Cake', 'description': '3-tier custom designed cake', 'included': True},
                {'service_name': 'Premium Florals', 'description': 'Premium centerpieces, bouquets, and arrangements', 'included': True},
                {'service_name': 'Full Event Planning', 'description': 'Complete planning from start to finish', 'included': True},
                {'service_name': 'Bridal Suite', 'description': 'Bridal suite preparation and makeup', 'included': True},
                {'service_name': 'Transportation', 'description': 'Bridal car and guest transportation', 'included': True},
                {'service_name': 'Lighting & Effects', 'description': 'Professional lighting and special effects', 'included': True},
            ]
        },
        {
            'name': 'Premium Wedding Package',
            'description': 'Luxury package with all premium services. Perfect for couples who want the best of everything for their special day.',
            'price': 15000.00,
            'guest_capacity_min': 150,
            'guest_capacity_max': 300,
            'features': '''Luxury venue decoration
Premium photography (12 hours) + Cinematic videography
Gourmet catering with live stations
Premium entertainment (live band + DJ)
Designer wedding cake
Luxury floral arrangements
Complete wedding planning
Bridal and groom suite preparation
Luxury transportation
Premium lighting and special effects
Photo booth
Wedding favors
Rehearsal dinner coordination''',
            'services': [
                {'service_name': 'Luxury Decoration', 'description': 'Designer-level decoration with custom themes', 'included': True},
                {'service_name': 'Premium Photography & Videography', 'description': '12 hours coverage with cinematic video', 'included': True},
                {'service_name': 'Gourmet Catering', 'description': 'Multi-course gourmet meal with live cooking stations', 'included': True},
                {'service_name': 'Premium Entertainment', 'description': 'Live band and premium DJ with MC', 'included': True},
                {'service_name': 'Designer Wedding Cake', 'description': 'Multi-tier designer cake', 'included': True},
                {'service_name': 'Luxury Florals', 'description': 'Premium designer floral arrangements', 'included': True},
                {'service_name': 'Complete Planning', 'description': 'Full-service wedding planning', 'included': True},
                {'service_name': 'Bridal & Groom Suite', 'description': 'Luxury suite preparation for both', 'included': True},
                {'service_name': 'Luxury Transportation', 'description': 'Premium vehicles for bridal party', 'included': True},
                {'service_name': 'Premium Lighting', 'description': 'Professional lighting design and effects', 'included': True},
                {'service_name': 'Photo Booth', 'description': 'Professional photo booth with props', 'included': True},
                {'service_name': 'Wedding Favors', 'description': 'Custom wedding favors for all guests', 'included': True},
                {'service_name': 'Rehearsal Dinner', 'description': 'Coordination for rehearsal dinner', 'included': True},
            ]
        },
        {
            'name': 'Luxury Wedding Package',
            'description': 'The ultimate wedding experience with every luxury service included. For couples who want nothing but the absolute best.',
            'price': 30000.00,
            'guest_capacity_min': 200,
            'guest_capacity_max': 500,
            'features': '''Ultra-luxury venue decoration
Elite photography (full day) + Cinematic film production
World-class gourmet catering
A-list entertainment
Designer multi-tier cake
Exotic floral arrangements
Concierge-level wedding planning
Luxury bridal and groom suites
Chauffeur service
Elite lighting and production
Professional photo booth
Premium wedding favors
Rehearsal dinner and welcome party
Day-after brunch
Honeymoon planning assistance''',
            'services': [
                {'service_name': 'Ultra-Luxury Decoration', 'description': 'Designer-level decoration with exotic themes', 'included': True},
                {'service_name': 'Elite Photography & Film', 'description': 'Full day coverage with cinematic film production', 'included': True},
                {'service_name': 'World-Class Catering', 'description': 'Gourmet multi-course meal with celebrity chef options', 'included': True},
                {'service_name': 'A-List Entertainment', 'description': 'Premium live band, DJ, and special performances', 'included': True},
                {'service_name': 'Designer Multi-Tier Cake', 'description': 'Custom designer cake with multiple flavors', 'included': True},
                {'service_name': 'Exotic Florals', 'description': 'Exotic and premium floral arrangements', 'included': True},
                {'service_name': 'Concierge Planning', 'description': 'White-glove wedding planning service', 'included': True},
                {'service_name': 'Luxury Suites', 'description': 'Premium suite preparation for entire bridal party', 'included': True},
                {'service_name': 'Chauffeur Service', 'description': 'Luxury chauffeur service for all guests', 'included': True},
                {'service_name': 'Elite Production', 'description': 'Professional lighting, sound, and production', 'included': True},
                {'service_name': 'Premium Photo Booth', 'description': 'Professional photo booth with instant prints', 'included': True},
                {'service_name': 'Premium Favors', 'description': 'Luxury wedding favors and gifts', 'included': True},
                {'service_name': 'Welcome Party', 'description': 'Rehearsal dinner and welcome party coordination', 'included': True},
                {'service_name': 'Day-After Brunch', 'description': 'Post-wedding brunch for all guests', 'included': True},
                {'service_name': 'Honeymoon Planning', 'description': 'Assistance with honeymoon planning', 'included': True},
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


def remove_default_packages(apps, schema_editor):
    """Remove default packages"""
    Package = apps.get_model('packages', 'Package')
    
    package_names = [
        'Basic Wedding Package',
        'Standard Wedding Package',
        'Premium Wedding Package',
        'Luxury Wedding Package'
    ]
    
    Package.objects.filter(name__in=package_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_packages, remove_default_packages),
    ]

