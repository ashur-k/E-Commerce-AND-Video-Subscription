from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_home, name="videos_home"),
    path('all_videos/', views.all_videos, name="all_videos"),
    path('pin_video/<int:video_id>/', views.pin_video, name='pin_video'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
    path('play_video/delete_video/<int:video_id>/', views.play_video, name="play_video"),
]