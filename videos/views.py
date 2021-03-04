from django.shortcuts import render
from .models import Video


def videos_home(request):
    videos = Video.objects.all()
    for video in videos:
        print(video.video_URL)
    template = 'videos/videos_home.html'
    context = {
        
    }
    return render(request, template , context)
