from django.db import models

TYPES = (
    ('Driveway', 'Driveway'),
    ('Lot', 'Lot'),
    ('Garage', 'Garage'),
    ('Street', 'Street'),
    ('Other', 'Other')
)

# Create your models here.
class Spot(models.Model):
    location = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=TYPES,
        default=TYPES[3][0]
    )
    price = models.IntegerField()

    def __str__(self):
        return self.location