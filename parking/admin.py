from django.contrib import admin
from .models import Location, Spot, Reservation

admin.site.register(Location)
admin.site.register(Spot)
admin.site.register(Reservation)