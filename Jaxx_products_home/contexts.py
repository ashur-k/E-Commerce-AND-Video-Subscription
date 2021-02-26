from products.models import Category


def navbar_categories(request):
    clothing_categories = Category.objects.filter(parent_name='clothing')
    homeware_categories = Category.objects.filter(parent_name='homeware')
    
    context = {
        'clothing_categories': clothing_categories,
        'homeware_categories': homeware_categories,
    }

    return context