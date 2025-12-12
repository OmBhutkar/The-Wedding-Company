# Generated manually to add sample vendors

from django.db import migrations
from decimal import Decimal


def create_sample_vendors(apps, schema_editor):
    """Create sample vendors for different categories"""
    VendorCategory = apps.get_model('vendors', 'VendorCategory')
    Vendor = apps.get_model('vendors', 'Vendor')
    
    # Get categories
    photography_category = VendorCategory.objects.filter(name='Photography').first()
    catering_category = VendorCategory.objects.filter(name='Catering').first()
    decoration_category = VendorCategory.objects.filter(name='Decoration').first()
    music_category = VendorCategory.objects.filter(name='Music & Entertainment').first()
    makeup_category = VendorCategory.objects.filter(name='Makeup & Beauty').first()
    transportation_category = VendorCategory.objects.filter(name='Transportation').first()
    lighting_category = VendorCategory.objects.filter(name='Lighting & Sound').first()
    planner_category = VendorCategory.objects.filter(name='Wedding Planner').first()
    cake_category = VendorCategory.objects.filter(name='Cake & Desserts').first()
    
    vendors_data = [
        # Photography Vendors
        {
            'name': 'Dream Lens Photography',
            'category': photography_category,
            'contact_person': 'Rajesh Kumar',
            'email': 'rajesh@dreamlens.com',
            'phone': '+91 98765 43210',
            'address': '123 MG Road, Mumbai, Maharashtra 400001',
            'service_description': 'Professional wedding photography with 10+ years of experience. Specializing in candid and traditional photography. Includes pre-wedding, wedding day, and post-wedding shoots.',
            'base_price': Decimal('50000.00'),
            'rating': Decimal('4.8'),
            'is_active': True,
            'notes': 'Available for destination weddings. Premium equipment and editing included.'
        },
        {
            'name': 'Memories Captured Studio',
            'category': photography_category,
            'contact_person': 'Priya Sharma',
            'email': 'priya@memoriescaptured.com',
            'phone': '+91 98765 43211',
            'address': '456 Bandra West, Mumbai, Maharashtra 400050',
            'service_description': 'Creative wedding photography with cinematic style. Expert in outdoor and indoor shoots. Full day coverage with multiple photographers.',
            'base_price': Decimal('75000.00'),
            'rating': Decimal('4.9'),
            'is_active': True,
            'notes': 'Award-winning photographer. Includes drone photography.'
        },
        
        # Catering Vendors
        {
            'name': 'Royal Feast Caterers',
            'category': catering_category,
            'contact_person': 'Amit Patel',
            'email': 'amit@royalfeast.com',
            'phone': '+91 98765 43212',
            'address': '789 Andheri East, Mumbai, Maharashtra 400069',
            'service_description': 'Premium catering services with multi-cuisine options. Specializing in North Indian, South Indian, Continental, and Chinese cuisine. Live counters and buffet arrangements.',
            'base_price': Decimal('60000.00'),
            'rating': Decimal('4.7'),
            'is_active': True,
            'notes': 'Can accommodate 50-500 guests. Halal and vegetarian options available.'
        },
        {
            'name': 'Gourmet Delights',
            'category': catering_category,
            'contact_person': 'Sneha Desai',
            'email': 'sneha@gourmetdelights.com',
            'phone': '+91 98765 43213',
            'address': '321 Juhu, Mumbai, Maharashtra 400049',
            'service_description': 'Luxury catering with international cuisine. Customized menus, live cooking stations, and premium presentation. Expert chefs and professional service staff.',
            'base_price': Decimal('120000.00'),
            'rating': Decimal('4.9'),
            'is_active': True,
            'notes': 'Fine dining experience. Can provide celebrity chefs on request.'
        },
        
        # Decoration Vendors
        {
            'name': 'Elegant Decorations',
            'category': decoration_category,
            'contact_person': 'Vikram Singh',
            'email': 'vikram@elegantdecor.com',
            'phone': '+91 98765 43214',
            'address': '654 Powai, Mumbai, Maharashtra 400076',
            'service_description': 'Complete wedding decoration services including stage setup, mandap decoration, floral arrangements, lighting, and theme-based designs.',
            'base_price': Decimal('80000.00'),
            'rating': Decimal('4.6'),
            'is_active': True,
            'notes': 'Specializes in traditional and modern themes. Includes setup and cleanup.'
        },
        {
            'name': 'Blossom Events',
            'category': decoration_category,
            'contact_person': 'Anjali Mehta',
            'email': 'anjali@blossomevents.com',
            'phone': '+91 98765 43215',
            'address': '987 Worli, Mumbai, Maharashtra 400018',
            'service_description': 'Premium floral decoration and event styling. Custom themes, luxury flower arrangements, and elegant setups. Expert designers and florists.',
            'base_price': Decimal('150000.00'),
            'rating': Decimal('4.8'),
            'is_active': True,
            'notes': 'Uses premium imported flowers. Can create custom installations.'
        },
        
        # Music & Entertainment Vendors
        {
            'name': 'DJ Ravi Sounds',
            'category': music_category,
            'contact_person': 'Ravi Malhotra',
            'email': 'ravi@djravisounds.com',
            'phone': '+91 98765 43216',
            'address': '147 Borivali, Mumbai, Maharashtra 400092',
            'service_description': 'Professional DJ services with premium sound system. Specializing in Bollywood, English, and regional music. MC services included.',
            'base_price': Decimal('35000.00'),
            'rating': Decimal('4.5'),
            'is_active': True,
            'notes': '15+ years experience. Can provide backup equipment.'
        },
        {
            'name': 'Melody Band',
            'category': music_category,
            'contact_person': 'Arjun Kapoor',
            'email': 'arjun@melodyband.com',
            'phone': '+91 98765 43217',
            'address': '258 Vashi, Navi Mumbai, Maharashtra 400703',
            'service_description': 'Live band performance with professional musicians. Can perform Bollywood hits, classical, and fusion music. Includes sound system and stage setup.',
            'base_price': Decimal('100000.00'),
            'rating': Decimal('4.7'),
            'is_active': True,
            'notes': '5-piece band. Can customize playlist as per requirements.'
        },
        
        # Makeup & Beauty Vendors
        {
            'name': 'Glamour Makeup Studio',
            'category': makeup_category,
            'contact_person': 'Neha Gupta',
            'email': 'neha@glamourmakeup.com',
            'phone': '+91 98765 43218',
            'address': '369 Lokhandwala, Mumbai, Maharashtra 400053',
            'service_description': 'Professional bridal makeup and hair styling. Includes trial sessions, bridal party makeup, and hair styling. Uses premium products.',
            'base_price': Decimal('25000.00'),
            'rating': Decimal('4.8'),
            'is_active': True,
            'notes': 'Expert in traditional and modern looks. Includes touch-up kit.'
        },
        {
            'name': 'Beauty by Riya',
            'category': makeup_category,
            'contact_person': 'Riya Shah',
            'email': 'riya@beautybyriya.com',
            'phone': '+91 98765 43219',
            'address': '741 Khar, Mumbai, Maharashtra 400052',
            'service_description': 'Luxury bridal makeup and hair services. Celebrity makeup artist with international experience. Customized looks and premium products.',
            'base_price': Decimal('50000.00'),
            'rating': Decimal('4.9'),
            'is_active': True,
            'notes': 'Award-winning makeup artist. Available for destination weddings.'
        },
        
        # Transportation Vendors
        {
            'name': 'Royal Wheels',
            'category': transportation_category,
            'contact_person': 'Manish Agarwal',
            'email': 'manish@royalwheels.com',
            'phone': '+91 98765 43220',
            'address': '852 Thane, Maharashtra 400601',
            'service_description': 'Premium car rental services for weddings. Collection includes luxury sedans, SUVs, and vintage cars. Professional chauffeurs included.',
            'base_price': Decimal('15000.00'),
            'rating': Decimal('4.6'),
            'is_active': True,
            'notes': 'Fleet includes BMW, Mercedes, Audi. Can arrange convoy for guests.'
        },
        {
            'name': 'Elite Transport Services',
            'category': transportation_category,
            'contact_person': 'Karan Mehta',
            'email': 'karan@elitetransport.com',
            'phone': '+91 98765 43221',
            'address': '963 Chembur, Mumbai, Maharashtra 400071',
            'service_description': 'Luxury transportation with premium vehicles. Includes bridal car decoration, guest transportation, and airport transfers. Professional service.',
            'base_price': Decimal('30000.00'),
            'rating': Decimal('4.7'),
            'is_active': True,
            'notes': 'Can provide luxury buses for guest transportation.'
        },
        
        # Lighting & Sound Vendors
        {
            'name': 'Bright Events Lighting',
            'category': lighting_category,
            'contact_person': 'Suresh Nair',
            'email': 'suresh@brightevents.com',
            'phone': '+91 98765 43222',
            'address': '159 Kurla, Mumbai, Maharashtra 400070',
            'service_description': 'Professional lighting and sound system setup. Includes stage lighting, ambient lighting, sound system, and microphones. Technical support included.',
            'base_price': Decimal('40000.00'),
            'rating': Decimal('4.6'),
            'is_active': True,
            'notes': 'Can create custom lighting designs. Backup equipment available.'
        },
        
        # Wedding Planner Vendors
        {
            'name': 'Perfect Day Planners',
            'category': planner_category,
            'contact_person': 'Rohit Verma',
            'email': 'rohit@perfectday.com',
            'phone': '+91 98765 43223',
            'address': '357 Santacruz, Mumbai, Maharashtra 400054',
            'service_description': 'Complete wedding planning services from concept to execution. Includes vendor coordination, timeline management, and day-of coordination.',
            'base_price': Decimal('200000.00'),
            'rating': Decimal('4.9'),
            'is_active': True,
            'notes': 'Full-service planning. Can handle destination weddings.'
        },
        
        # Cake & Desserts Vendors
        {
            'name': 'Sweet Dreams Bakery',
            'category': cake_category,
            'contact_person': 'Pooja Reddy',
            'email': 'pooja@sweetdreams.com',
            'phone': '+91 98765 43224',
            'address': '468 Goregaon, Mumbai, Maharashtra 400062',
            'service_description': 'Custom wedding cakes and dessert arrangements. Multi-tier cakes, cupcakes, and dessert tables. Various flavors and designs available.',
            'base_price': Decimal('20000.00'),
            'rating': Decimal('4.7'),
            'is_active': True,
            'notes': 'Can create themed cakes. Sugar-free options available.'
        },
        {
            'name': 'Luxury Cakes & More',
            'category': cake_category,
            'contact_person': 'Aditi Joshi',
            'email': 'aditi@luxurycakes.com',
            'phone': '+91 98765 43225',
            'address': '579 Malad, Mumbai, Maharashtra 400064',
            'service_description': 'Premium designer wedding cakes and luxury dessert arrangements. Custom designs, premium ingredients, and elegant presentation.',
            'base_price': Decimal('45000.00'),
            'rating': Decimal('4.8'),
            'is_active': True,
            'notes': 'Award-winning cake designer. Can create elaborate multi-tier designs.'
        },
    ]
    
    for vendor_data in vendors_data:
        Vendor.objects.get_or_create(
            name=vendor_data['name'],
            defaults=vendor_data
        )


def remove_sample_vendors(apps, schema_editor):
    """Remove sample vendors"""
    Vendor = apps.get_model('vendors', 'Vendor')
    
    vendor_names = [
        'Dream Lens Photography', 'Memories Captured Studio',
        'Royal Feast Caterers', 'Gourmet Delights',
        'Elegant Decorations', 'Blossom Events',
        'DJ Ravi Sounds', 'Melody Band',
        'Glamour Makeup Studio', 'Beauty by Riya',
        'Royal Wheels', 'Elite Transport Services',
        'Bright Events Lighting',
        'Perfect Day Planners',
        'Sweet Dreams Bakery', 'Luxury Cakes & More'
    ]
    
    Vendor.objects.filter(name__in=vendor_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_add_default_categories'),
    ]

    operations = [
        migrations.RunPython(create_sample_vendors, remove_sample_vendors),
    ]


