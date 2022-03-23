from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='get_routes'),
    path('get-projects/', views.get_projects, name='get_projects'),
    path('get-projects/<str:pk>/', views.get_project, name='get_project'),
]
