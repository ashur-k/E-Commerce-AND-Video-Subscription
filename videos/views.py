from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib import messages
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

def all_videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    template = "videos/all_videos.html"
    return render (request, template, context)


def delete_video(request, video_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    video = get_object_or_404(Video, pk=video_id)
    video.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('all_products')