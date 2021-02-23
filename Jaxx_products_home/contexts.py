from products.models import Category


def navbar_categories(request):
    clothing_categories = Category.objects.filter(parent_name='Clothing')
    print(clothing_categories)
    for item in clothing_categories:
        print(item.status)
    context = {
        'clothing_categories': clothing_categories,
    }

    return context