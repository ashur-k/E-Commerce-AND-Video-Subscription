from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_home, name="videos_home"),
    path('all_videos/', views.all_videos, name="all_videos"),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
]