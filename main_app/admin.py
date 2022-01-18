from django.contrib import admin
from .models import Spot, Booking, Feature, Photo

# Register your models here.
admin.site.register(Spot)
admin.site.register(Booking)
admin.site.register(Feature)
admin.site.register(Photo)