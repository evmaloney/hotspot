from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Spot, Feature
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
  return HttpResponse('<h1>hello</h1>')

def about(request):
  return render(request, 'about.html')

def spots_index(request):
  spots = Spot.objects.all()
  return render(request, 'spots/index.html', {'spots': spots})

def spots_detail(request, spot_id):
  if request.user.spot_set.filter(id=spot_id).exists():
    spot = Spot.objects.get(id=spot_id)
    features_spot_doesnt_have = Feature.objects.exclude(id__in = spot.features.all().values_list('id'))
    # instantiate BookingForm to be rendered in the template
    booking_form = BookingForm()
    return render(request, 'spots/detail.html', {
      'spot': spot, 'booking_form': booking_form,
      'features': features_spot_doesnt_have
    })
  else:
    return redirect('index')