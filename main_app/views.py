from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Spot, Feature, Photo, Booking
from .forms import BookingForm
import uuid
import boto3
import os


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def spots_index(request):
  spots = Spot.objects.all()
  return render(request, 'spots/index.html', {'spots': spots})

@login_required
def myspots_index(request, user_id):
  spots = Spot.objects.filter(user_id=request.user.id)
  return render(request, 'spots/myindex.html', {'spots': spots})

@login_required
def spots_detail(request, spot_id):
  spot = Spot.objects.get(id=spot_id)
  features_spot_doesnt_have = Feature.objects.exclude(id__in = spot.features.all().values_list('id'))
  # instantiate BookingForm to be rendered in the template
  booking_form = BookingForm()
  return render(request, 'spots/detail.html', {
    'spot': spot, 'booking_form': booking_form,
    'features': features_spot_doesnt_have
  })

@login_required
def add_booking(request, spot_id):
  spot = Spot.objects.get(id=spot_id)
  # create a ModelForm instance using the data in request.POST
  form = BookingForm(request.POST)
  # Validate the form!
  if form.is_valid():
    # don't save the form to th db until it has the cat_id assigned to it
    new_booking = form.save(commit=False)
    new_booking.spot_id = spot_id
    if (Booking.objects.filter(spot_id=spot_id).filter(date=new_booking.date).exists() == False) and (spot.user == request.user):
      print(request.user.id)
      new_booking.save()
      print(new_booking.id)
  return redirect('detail', spot_id=spot_id)

@login_required
def assoc_feature(request, spot_id, feature_id):
  # Note that you can pass a feature's id instead of the whole feature object
  Spot.objects.get(id=spot_id).features.add(feature_id)
  return redirect('detail', spot_id=spot_id)

@login_required
def add_photo(request, spot_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client('s3')
    #need a unique key for s3 & needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # in case something goes wrong
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      # build the full url string
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      # we can assign to spot_id or spot (if you have a spot object)
      Photo.objects.create(url=url, spot_id=spot_id)
    except:
      print('An error occurred uplaoding file to S3')
  return redirect('detail', spot_id=spot_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# Class-Based views
class SpotCreate(LoginRequiredMixin, CreateView):
  model = Spot
  # fields = '__all__'
  # success_url = '/spots/'
  fields = ['address', 'type', 'price', 'description']

  # this inherited is called when a valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class SpotUpdate(LoginRequiredMixin, UpdateView):
  model = Spot
  # Let's dissallow the renaming of a cat by excluding the name field!
  fields = ['type', 'price', 'description']

class SpotDelete(LoginRequiredMixin, DeleteView):
  model = Spot
  success_url = '/spots/'

class FeatureList(LoginRequiredMixin, ListView):
  model = Feature

class FeatureDetail(LoginRequiredMixin, DetailView):
  model = Feature

class FeatureCreate(LoginRequiredMixin, CreateView):
  model = Feature
  fields = '__all__'

class FeatureUpdate(LoginRequiredMixin, UpdateView):
  model = Feature
  fields = ['name']

class FeatureDelete(LoginRequiredMixin, DeleteView):
  model = Feature
  success_url = '/features/'