from django.db import models
from django.utils import timezone
import pytz

class Location(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=50)  
    
    def __str__(self):
        return self.name

class Spot(models.Model):
    number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location.name} - Spot {self.number}"

class Reservation(models.Model):
    plate_number = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20, default='DEFAULT_ID')  # Add default value here
    spot = models.OneToOneField(Spot, on_delete=models.CASCADE)
    date_reserved = models.DateTimeField(default=timezone.now)

    def get_local_date_reserved(self):
        philippine_tz = pytz.timezone('Asia/Manila')
        return self.date_reserved.astimezone(philippine_tz)

    def __str__(self):
        return f"Reservation for {self.plate_number} at {self.spot.number}"