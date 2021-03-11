from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Video, VideoCategory


def videos_home(request):
    videos = Video.objects.all()
    my_video = get_object_or_404(Video, id=9)
    template = 'videos/videos_home.html'
    context = {
        'videos': videos,
        'my_video': my_video,
    }
    return render(request, template , context)

def all_videos(request):
    videos = Video.objects.all()
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            
            videos = videos.filter(video_category__video_category__in=categories)         
            categories = VideoCategory.objects.filter(video_category__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria")
                    return redirect(reverse('videos_home'))        

                queries = Q(video_name__icontains=query) | Q(video_description__icontains=query)
                products = products.filter(queries)
                messages.success(request, f'{videos.count()} results found.')

    
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
    if request.method == 'POST':
        video = get_object_or_404(Video, pk=video_id)
        video.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('all_videos')