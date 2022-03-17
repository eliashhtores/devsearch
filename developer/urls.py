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
    path('add-skill/', views.create_skill, name='add_skill'),
    path('edit-skill/<str:pk>', views.edit_skill, name='edit_skill'),
    path('delete-skill/<str:pk>', views.delete_skill, name='delete_skill'),
    path('inbox/', views.inbox, name='inbox')
]
