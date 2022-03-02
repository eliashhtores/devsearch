from django.urls import path
from . import views

app_name = 'developer'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('edit-account/', views.edit_account, name='edit_account'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile'),
]
