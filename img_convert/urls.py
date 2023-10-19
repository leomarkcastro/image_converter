
from django.urls import path
from . import views

urlpatterns = [
    path('simple', views.simple_upload, name='simple_upload'),
    path('auth', views.auth_page, name='auth'),
]
