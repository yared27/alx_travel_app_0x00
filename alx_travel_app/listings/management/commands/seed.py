from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with fake listings'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                price_per_night=random.randint(100, 1000),
                location=fake.city()
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with fake listings'))
