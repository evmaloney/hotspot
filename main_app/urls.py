from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name="about"),
  path('spots/', views.spots_index, name="index"),
]
# k