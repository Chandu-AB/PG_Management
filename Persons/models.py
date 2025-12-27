from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=14, unique=True)
    address = models.TextField(null=True, blank=True)
    room_no = models.ForeignKey("Rooms.Room", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
