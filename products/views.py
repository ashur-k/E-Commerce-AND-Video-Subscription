from django.shortcuts import render


def products(request):
    ''' All Products serach and dispaly will be
        get managed in this view
    '''
    context = {
        
    }
    template ='products/products.html'
    return render (request, template, context)