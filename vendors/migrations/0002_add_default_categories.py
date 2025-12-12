# Generated manually to add default vendor categories

from django.db import migrations


def create_default_categories(apps, schema_editor):
    """Create default vendor categories"""
    VendorCategory = apps.get_model('vendors', 'VendorCategory')
    
    categories = [
        {'name': 'Photography', 'description': 'Wedding photography and videography services'},
        {'name': 'Catering', 'description': 'Food and beverage services for weddings'},
        {'name': 'Decoration', 'description': 'Wedding decoration and floral arrangements'},
        {'name': 'Music & Entertainment', 'description': 'DJ, live music, and entertainment services'},
        {'name': 'Venue', 'description': 'Wedding venues and event spaces'},
        {'name': 'Makeup & Beauty', 'description': 'Bridal makeup, hair styling, and beauty services'},
        {'name': 'Transportation', 'description': 'Wedding transportation and car rental services'},
        {'name': 'Lighting & Sound', 'description': 'Professional lighting and sound system services'},
        {'name': 'Wedding Planner', 'description': 'Full-service wedding planning and coordination'},
        {'name': 'Invitation & Stationery', 'description': 'Wedding invitations, cards, and stationery'},
        {'name': 'Cake & Desserts', 'description': 'Wedding cakes and dessert services'},
        {'name': 'Security', 'description': 'Event security and safety services'},
    ]
    
    for category_data in categories:
        VendorCategory.objects.get_or_create(
            name=category_data['name'],
            defaults={'description': category_data['description']}
        )


def remove_default_categories(apps, schema_editor):
    """Remove default vendor categories"""
    VendorCategory = apps.get_model('vendors', 'VendorCategory')
    
    category_names = [
        'Photography', 'Catering', 'Decoration', 'Music & Entertainment',
        'Venue', 'Makeup & Beauty', 'Transportation', 'Lighting & Sound',
        'Wedding Planner', 'Invitation & Stationery', 'Cake & Desserts', 'Security'
    ]
    
    VendorCategory.objects.filter(name__in=category_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, remove_default_categories),
    ]


