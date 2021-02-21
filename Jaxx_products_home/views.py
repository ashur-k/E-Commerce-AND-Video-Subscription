from django.shortcuts import render


def homepage(request):
    template = "Jaxx_products_home/homepage.html"
    context = {
        "page_heading": "jAxx pRoductions"
    }
    return render(request, template, context)
