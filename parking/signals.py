from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Location, Spot

@receiver(post_migrate)
def create_locations_and_spots(sender, **kwargs):
    if sender.name == 'parking':
        locations = [
            {"name": "JSEC Central Carpark", "capacity": 50},
            {"name": "Covered Courts - Upper East Carpark", "capacity": 50},
            {"name": "Covered Courts - Lower East Carpark", "capacity": 50},
            {"name": "Arete - North West Carpark", "capacity": 50},
            {"name": "Bellarmine Carpark", "capacity": 50},
        ]

        for loc in locations:
            location, created = Location.objects.get_or_create(name=loc["name"], defaults={"capacity": loc["capacity"]})
            if created:  # Only add spots if the location was newly created
                for i in range(1, 51):
                    Spot.objects.create(number=f"Spot {i}", is_available=True, location=location)
