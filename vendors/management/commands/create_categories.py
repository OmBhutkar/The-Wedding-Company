"""
Management command to create default vendor categories
Usage: python manage.py create_categories
"""
from django.core.management.base import BaseCommand
from vendors.models import VendorCategory


class Command(BaseCommand):
    help = 'Creates default vendor categories'

    def handle(self, *args, **options):
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
        
        created_count = 0
        for category_data in categories:
            category, created = VendorCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⊘ Category already exists: {category.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nTotal categories: {VendorCategory.objects.count()}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'New categories created: {created_count}')
        )


