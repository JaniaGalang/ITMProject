from django.core.management.base import BaseCommand
from parking.models import Location, Spot

class Command(BaseCommand):
    help = 'Populate the parking locations and spots'

    def handle(self, *args, **kwargs):
        locations = [
            {"name": "JSEC Central Carpark", "capacity": 50},
            {"name": "Covered Courts - Upper East Carpark", "capacity": 50},
            {"name": "Covered Courts - Lower East Carpark", "capacity": 50},
            {"name": "Arete - North West Carpark", "capacity": 50},
            {"name": "Bellarmine Carpark", "capacity": 50},
            {"name": "ISO - North Carpark", "capacity": 50},
        ]

        for loc in locations:
            location, created = Location.objects.get_or_create(name=loc["name"], defaults={"capacity": loc["capacity"]})
            if created:  # Only add spots if the location was newly created
                for i in range(1, 51):
                    Spot.objects.create(number=f"{i}", is_available=True, location=location)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated locations and spots'))
