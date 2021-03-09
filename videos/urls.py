from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_home, name="videos_home")
]