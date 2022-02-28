from django.urls import path
from . import views

app_name = 'developer'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile'),
]
