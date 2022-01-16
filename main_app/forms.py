from ast import Mod
from pyexpat import model
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Booking 

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['startdate', 'enddate']