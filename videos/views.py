from django.shortcuts import render, get_object_or_404
from .models import Video


def videos_home(request):
    videos = Video.objects.all()
    my_video = get_object_or_404(Video, id=1)
    template = 'videos/videos_home.html'
    context = {
        'videos': videos,
        'my_video': my_video,
    }
    return render(request, template , context)
