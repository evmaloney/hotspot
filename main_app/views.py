from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse('<h1>hello</h1>')

def about(request):
  return render(request, 'about.html')

def spots_index(request):
  return render(request, 'spots/index.html', {'spots': spots})
