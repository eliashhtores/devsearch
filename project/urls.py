from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:pk>', views.project, name='project'),
    path('create-project', views.create_project, name='create_project'),
    path('update-project/<str:pk>',
         views.update_project, name='update_project'),
    path('delete-project/<str:pk>',
         views.delete_project, name='delete_project'),
]
