from django.db import models

class Vehicle(models.Model):
    number_plate=models.CharField(max_length=20)
    vehicle_type=models.CharField(max_length=20)
    manufacturer=models.CharField(max_length=20)
    year=models.IntegerField()

def __str__(self):
    return f"{self.number_plate} - {self.vehicle_type}"

# Create your models here.
