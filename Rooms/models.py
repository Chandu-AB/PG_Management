from django.db import models
from Persons.models import Person

class Room(models.Model):

    room_no = models.CharField(max_length=10, primary_key=True)  # PK, no auto-increment)  # Room number
    floor_no = models.IntegerField()                         # Floor number
    no_beds = models.IntegerField()                          # Number of beds
    is_available = models.BooleanField(default=True)        # Availability status

    def __str__(self):
        status = "Available" if self.is_available else "Occupied"
        return f"Room {self.room_no} (Floor {self.floor_no}, Beds: {self.no_beds}, {status})"

    
    
    @property
    def active_persons(self):
        return self.person_set.filter(is_active=True).count()

    @property
    def available_beds(self):
        return self.no_beds - self.active_persons
    @property
    def is_full(self):
        return self.active_persons >= self.no_beds 

    def __str__(self):
        return f"Room {self.room_no}"