from django.shortcuts import render
from django.http import HttpResponse

class Spot:
    def __init__(self, location, type, price):
        self.location = location
        self.type = type
        self.price = price 
spots = [
  Spot('LA', 'gated', '100'),
  Spot('Koreatown', 'outside', '200'),
  Spot('Torrance', 'street', '300')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>hello</h1>')

def about(request):
  return render(request, 'about.html')

def spots_index(request):
  return render(request, 'spots/index.html', {'spots': spots})
