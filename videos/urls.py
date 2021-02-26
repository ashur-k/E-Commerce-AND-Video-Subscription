from django.urls import path
from . import views

urlpatterns = [
    path('videos_home', views.videos_home, name="videos_home")
]