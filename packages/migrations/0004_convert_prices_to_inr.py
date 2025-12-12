# Migration to convert package prices from USD to INR
# Conversion rate: 1 USD = 83 INR (approximate)

from django.db import migrations


def convert_prices_to_inr(apps, schema_editor):
    """Convert all package prices from USD to INR"""
    Package = apps.get_model('packages', 'Package')
    USD_TO_INR = 83  # Conversion rate
    
    packages = Package.objects.all()
    for package in packages:
        # Convert price from USD to INR
        package.price = package.price * USD_TO_INR
        package.save()


def convert_prices_back_to_usd(apps, schema_editor):
    """Convert prices back to USD (for rollback)"""
    Package = apps.get_model('packages', 'Package')
    USD_TO_INR = 83
    
    packages = Package.objects.all()
    for package in packages:
        # Convert price back from INR to USD
        package.price = package.price / USD_TO_INR
        package.save()


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_add_more_packages'),
    ]

    operations = [
        migrations.RunPython(convert_prices_to_inr, convert_prices_back_to_usd),
    ]


