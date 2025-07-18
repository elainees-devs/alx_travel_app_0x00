from django.core.management.base import BaseCommand
from listings.models import Property

class Command(BaseCommand):
    help = 'Seed the database with sample property listings'

    def handle(self, *args, **options):
        # Define sample listings data
        sample_listings = [
            {
                'title': 'Cozy Lake House',
                'description': 'A beautiful house by the lake with stunning views.',
                'location': 'Lakeview Drive, Lakeside',
                'price_per_night': 150.00
            },
            {
                'title': 'Modern City Apartment',
                'description': 'Stylish apartment in the city center close to everything.',
                'location': 'Downtown Avenue, Metropolis',
                'price_per_night': 120.00
            },
            {
                'title': 'Rustic Mountain Cabin',
                'description': 'Charming cabin in the mountains, perfect for a weekend getaway.',
                'location': 'Mountain Trail Road, Highlands',
                'price_per_night': 90.00
            }
        ]

        # Create listings
        for listing in sample_listings:
            Property.objects.create(**listing)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings!'))
