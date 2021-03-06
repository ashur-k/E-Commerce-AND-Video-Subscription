from products.models import Category
from videos.models import VideoCategory


def navbar_categories(request):
    #clothing_categories = Category.objects.filter(parent_name='clothing')
    #homeware_categories = Category.objects.filter(parent_name='homeware')
    video_categories = VideoCategory.objects.all()
    context = {
        # 'clothing_categories': clothing_categories,
        # 'homeware_categories': homeware_categories,
        'video_categories': video_categories
    }

    return context