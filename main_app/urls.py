from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name="about"),
  path('spots/', views.spots_index, name="index"),
  path('spots/user/<int:user_id>', views.myspots_index, name="myindex"),
  path('spots/<int:spot_id>', views.spots_detail, name='detail'),
  path('spots/create/', views.SpotCreate.as_view(), name='spots_create'),
  path('spots/<int:pk>/update/', views.SpotUpdate.as_view(), name='spots_update'),
  path('spots/<int:pk>/delete/', views.SpotDelete.as_view(), name='spots_delete'),
  path('spots/<int:spot_id>/add_booking/', views.add_booking, name='add_booking'),
  path('features/', views.FeatureList.as_view(), name='features_index'),
  path('features/<int:pk>/', views.FeatureDetail.as_view(), name='features_detail'),
  path('features/create/', views.FeatureCreate.as_view(), name='features_create'),
  path('features/<int:pk>/update/', views.FeatureUpdate.as_view(), name='features_update'),
  path('features/<int:pk>/delete/', views.FeatureDelete.as_view(), name='features_delete'),
  path('spots/<int:spot_id>/assoc_feature/<int:feature_id>/', views.assoc_feature, name='assoc_feature'),
  path('spots/<int:spot_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accounts/signup/', views.signup, name='signup'),
]
