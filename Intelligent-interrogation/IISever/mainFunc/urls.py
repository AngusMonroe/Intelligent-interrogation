from django.urls import path

from . import views

urlpatterns = [
    path('text', views.main_text, name='main_text'),
    path('file', views.main_file, name='main_file'),
]