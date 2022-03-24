from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('developer/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('developer/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('get-projects/', views.get_projects, name='get_projects'),
    path('get-projects/<str:pk>/', views.get_project, name='get_project'),
    path('project/<str:pk>/vote/', views.project_vote, name='project_vote'),
]
