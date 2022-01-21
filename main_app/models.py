from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('features_detail', kwargs={'pk': self.id})

# Create your models here.


class Spot(models.Model):
    address = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    features = models.ManyToManyField(Feature)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('detail', kwargs={'spot_id': self.id})


class Booking(models.Model):
    date = models.DateField('date')
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}'

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for spot_id: {self.spot_id} @{self.url}"
