from ctypes import addressof
import imp
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 

TYPES = (
    ('Driveway', 'Driveway'),
    ('Lot', 'Lot'),
    ('Garage', 'Garage'),
    ('Street', 'Street'),
    ('Other', 'Other')
)

# Create your models here.
class Spot(models.Model):
    address = models.CharField(max_length=150)
    type = models.CharField(
        max_length=15,
        choices=TYPES,
        default=TYPES[3][0]
    )
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address